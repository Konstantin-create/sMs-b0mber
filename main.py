# -*- coding: utf-8 -*- 
import datetime
import threading
import time
import traceback

import telebot
from telebot import types

import keyboards
import services
import texts
from config import connect

bot = telebot.TeleBot('5419285415:AAFF522ozCM7mrsJjZMJ0b3Z199IOrsanQ8')
admin_list = [1264066850]

last_time = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        if message.chat.id not in last_time:
            last_time[message.chat.id] = time.time()
            start_messages(message)
        else:
            if (time.time() - last_time[message.chat.id]) * 1000 < 1000:
                return 0
            else:
                start_messages(message)
            last_time[message.chat.id] = time.time()
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


def start_messages(message):
    userid = str(message.chat.id)
    connection, q = connect()
    q.execute(f'SELECT userid FROM ugc_users WHERE userid = "{userid}"')
    row = q.fetchone()
    if row is None:
        q.execute("INSERT INTO ugc_users (userid) VALUES ('%s')" % (userid))
        connection.commit()
        bot.send_message(message.chat.id, '<b>Главное меню ⤵️</b>', parse_mode='HTML', reply_markup=keyboards.main_menu)
    else:
        bot.send_message(message.chat.id, '<b>Главное меню ⤵️</b>', parse_mode='HTML', reply_markup=keyboards.main_menu)


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        if message.chat.id not in last_time:
            last_time[message.chat.id] = time.time()
            osnova_message(message)
        else:
            if (time.time() - last_time[message.chat.id]) * 1000 < 1000:
                return 0
            else:
                osnova_message(message)
            last_time[message.chat.id] = time.time()
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


def osnova_message(message):
    try:
        if str(message.chat.type) == 'private':
            if message.text == '/admin' and message.chat.id in admin_list:
                bot.send_message(message.chat.id, '<b>Держи менюшку</b>', parse_mode='HTML',
                                 reply_markup=keyboards.admin)

            if message.text == 'Статистика проекта' and message.chat.id in admin_list:
                bot.send_message(message.chat.id, f'<b>{texts.admin_stata()}</b>', parse_mode='HTML')

            if message.text == 'Рассылка' and message.chat.id in admin_list:
                msg = bot.send_message(message.chat.id, 'Введите текст рассылки', parse_mode='HTML')
                bot.register_next_step_handler(msg, send_photoorno)

            if message.text == 'Атака':
                mmsg = bot.send_message(message.chat.id, '<b>Введи номер телефона (без +)</b>', parse_mode='HTML')
                bot.register_next_step_handler(mmsg, phone)
            try:
                if message.text == 'Статистика':
                    bot.send_message(message.chat.id, texts.stata(), parse_mode='HTML')
            except:
                pass
            try:
                if message.text == 'Информация':
                    bot.send_message(message.chat.id,
                                     '<b>☺️ Мы ребята хоть куда, выебем все номера\nПо всем вопросам: @Вставь_сюда_что-то\n Чат: @Вставь_сюда_что-то</b>',
                                     parse_mode='HTML')
            except:
                pass
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        msg = call.data
        if 'start_bomber' in msg:
            answer = msg.split('#')
            connection, q = connect()
            q.execute(f'SELECT COUNT(id) FROM ugc_spam where phone = "{answer[1]}" and status = "1"')
            infa = q.fetchone()[0]
            if infa == 0:
                now = datetime.datetime.now()
                clock = now + datetime.timedelta(seconds=10)
                start_time = str(clock)[:16]
                q.execute("INSERT INTO ugc_spam (userid,phone,date_start,spam_time) VALUES ('%s','%s','%s','%s')" % (
                    call.message.chat.id, answer[1], start_time, answer[2]))
                connection.commit()
                am = threading.Thread(target=services.spam_ru,
                                      args=(answer[1], start_time, answer[2], call.message.chat.id)).start()
                bot.send_message(message.chat.id,
                                 f'Пользователь {call.message.chat.id} спамит на номер {answer[1]}, {answer[2]} минут')
                mmsg = bot.send_message(call.message.chat.id, '''<b>Бомбер запущен!</b>''', parse_mode='HTML')
            else:
                mmsg = bot.send_message(call.message.chat.id, '''<b>Номер уже бомбят</b>''', parse_mode='HTML')

        if msg == 'активные':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='<b>Список запущеных бомбилок:</b>', parse_mode='HTML',
                                  reply_markup=keyboards.activ_bomber(call.message.chat.id))

        if msg == "история":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='<b>Список всех бомбилок:</b>', parse_mode='HTML',
                                  reply_markup=keyboards.all_bomber(call.message.chat.id))

        if 'аинфа_' in msg:
            menu = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад', callback_data=f'активные'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.infa_bomb(msg[6:], call.message.chat.id), parse_mode='HTML',
                                  reply_markup=menu)

        if 'винфа_' in msg:
            menu = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='Назад', callback_data=f'история'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.infa_bomb(msg[6:], call.message.chat.id), parse_mode='HTML',
                                  reply_markup=menu)

        if 'линфа_' in msg:
            menu = types.InlineKeyboardMarkup()
            menu.add(types.InlineKeyboardButton(text='Удалить', callback_data=f'удаляем_{msg[6:]}'))
            menu.add(types.InlineKeyboardButton(text='Назад', callback_data=f'white_list'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f'Удаляем номер {msg[6:]} из белого списка?', parse_mode='HTML',
                                  reply_markup=menu)

        if 'удаляем_' in msg:
            connection, q = connect()
            q.execute(f'DELETE FROM ugc_white_list WHERE userid = "{call.message.chat.id}" and phone = "{msg[8:]}"')
            connection.commit()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.white_list(), parse_mode='HTML',
                                  reply_markup=keyboards.white_list(call.message.chat.id))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Номер удален!")

        if 'добавить_номер' in msg:
            mmsg = bot.send_message(call.message.chat.id, '<b>Введите номер (без +, пример: 79999999999)</b>',
                                    parse_mode='HTML')
            bot.register_next_step_handler(mmsg, add_white_list)

        if 'вернуться_главная' in msg:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='<b>Держи менюшку</b>', parse_mode='HTML', reply_markup=keyboards.menu)

        if msg == 'premium':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.premium_text(call.message.chat.id), parse_mode='HTML',
                                  reply_markup=keyboards.premium(call.message.chat.id))

        if msg == 'купить_прем':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.buy_premium(call.message.chat.id), parse_mode='HTML',
                                  reply_markup=keyboards.buy_premium(call.message.chat.id))

        if msg == 'получить_прем':
            menu = types.InlineKeyboardMarkup()
            menu.add(types.InlineKeyboardButton(text='Назад', callback_data=f'вернуться_главная'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.free_premium(call.message.chat.id), parse_mode='HTML', reply_markup=menu)
        if msg == 'white_list':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.white_list(), parse_mode='HTML',
                                  reply_markup=keyboards.white_list(call.message.chat.id))
    except Exception as e:
        bot.send_message(call.message.chat.id, traceback.format_exc())


def add_white_list(message):
    if message.text.isdigit() == True and len(message.text) >= 11:
        connection, q = connect()
        q.execute("INSERT INTO ugc_white_list (phone,userid) VALUES ('%s','%s')" % (message.text, message.chat.id))
        connection.commit()
        mmsg = bot.send_message(message.chat.id, '''<b>Номер добавлен в белый список</b>''', parse_mode='HTML')
    else:
        mmsg = bot.send_message(message.chat.id, '''<b>Вводить нужно номер телефона без +</b>''', parse_mode='HTML')


def phone(message):
    try:
        connection, q = connect()
        am = message.text
        if '+' in message.text:
            am = message.text.replace('+', '')
        if am.isdigit() == True:
            q.execute(f'SELECT COUNT(id) FROM ugc_spam where phone = "{am}" and status = "1"')
            infa = q.fetchone()[0]
            if infa == 0:
                mmsg = bot.send_message(message.chat.id, '''<b>Введи время спама\nОт 1 до 20 минут</b>''',
                                        parse_mode='HTML')
                bot.register_next_step_handler(mmsg, time_spam, am)
            else:
                mmsg = bot.send_message(message.chat.id, '''<b>Номер уже бомбят</b>''', parse_mode='HTML')
        else:
            mmsg = bot.send_message(message.chat.id, '''<b>Вводить нужно номер</b>''', parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


def time_send(message, phone):
    try:
        start_time = message.text
        if start_time == '+':
            now = datetime.datetime.now()
            clock = now + datetime.timedelta(minutes=1)
            start_time = str(clock)[:16]
        connection, q = connect()
        q.execute(f'SELECT * FROM ugc_users where userid = "{message.chat.id}"')
        infa = q.fetchone()
        mmsg = bot.send_message(message.chat.id, '''<b>Введи время спама\n\nОт 1 до 20 минут</b>''', parse_mode='HTML')
        bot.register_next_step_handler(mmsg, time_spam, phone)
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


def time_spam(message, phone):
    try:
        if message.text.isdigit() == True:
            connection, q = connect()
            q.execute(f'SELECT * FROM ugc_users where userid = "{message.chat.id}"')
            infa = q.fetchone()
            if int(message.text) >= 1 and int(message.text) <= 20:
                send_bomb = types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(text='Запустить', callback_data=f'start_bomber#{phone}#{message.text}'))
                mmsg = bot.send_message(message.chat.id,
                                        f'''<b>Номер: {phone}\nВремя спама: {message.text} мин\n</b>''',
                                        parse_mode='HTML', reply_markup=send_bomb)
            else:
                bot.send_message(message.chat.id, 'Минимум - 1 минута, максимум 20')
        else:
            bot.send_message(message.chat.id, 'Вводить нужно цифры!')
    except Exception as e:
        bot.send_message(message.chat.id, traceback.format_exc())


def send_photoorno(message):
    global text_send_all
    global json_entit
    text_send_all = message.text
    json_entit = None
    if 'entities' in message.json:
        json_entit = message.json['entities']
    msg = bot.send_message(message.chat.id,
                           '<b>Введите нужны аргументы в таком виде:\n\nНазвание рекламы\nСсылка на картинку\nКогда отправить</b>\n\nЕсли что-то из этого не нужно, то напишите "Нет", указывайте дату в таком формате: год-месяц-число часы:минуты (пример: 2020-12-09 15:34)',
                           parse_mode='HTML')
    bot.register_next_step_handler(msg, admin_send_message_all_text_rus)


def admin_send_message_all_text_rus(message):
    try:
        global photoo
        global keyboar
        global time_send
        global v
        time_send = message.text.split('\n')[2]
        photoo = message.text.split('\n')[1]
        keyboar = message.text.split('\n')[0]
        v = 0
        if str(photoo.lower()) != 'Нет'.lower():
            v = v + 1

        if str(keyboar.lower()) != 'Нет'.lower():
            v = v + 2

        if v == 0:
            msg = bot.send_message(message.chat.id,
                                   "Отправить всем пользователям уведомление:\n" + text_send_all + '\n\nЕсли вы согласны, напишите Да',
                                   parse_mode='HTML')
            bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)

        elif v == 1:
            msg = bot.send_photo(message.chat.id, str(photoo),
                                 "Отправить всем пользователям уведомление:\n" + text_send_all + '\n\nЕсли вы согласны, напишите Да',
                                 parse_mode='HTML')
            bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)

        elif v == 2:
            msg = bot.send_message(message.chat.id,
                                   "Отправить всем пользователям уведомление:\n" + text_send_all + '\n\nЕсли вы согласны, напишите Да',
                                   parse_mode='HTML')
            bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)

        elif v == 3:
            msg = bot.send_photo(message.chat.id, str(photoo),
                                 "Отправить всем пользователям уведомление:\n" + text_send_all + '\n\nЕсли вы согласны, напишите Да',
                                 parse_mode='HTML')
            bot.register_next_step_handler(msg, admin_send_message_all_text_da_rus)
    except:
        bot.send_message(message.chat.id, "Ошибка при вводе аргументов", parse_mode='HTML')


def admin_send_message_all_text_da_rus(message):
    otvet = message.text
    colvo_send_message_users = 0
    colvo_dont_send_message_users = 0
    if message.text.lower() == 'Да'.lower():
        if time_send.lower() == 'нет':
            pass

        else:
            connection, q = connect()
            q.execute("INSERT INTO ugc_temp_sending (text,image,button,date) VALUES ('%s','%s','%s','%s')" % (
                text_send_all, photoo, keyboar, time_send))
            connection.commit()
            q.execute('update ugc_temp_sending set entit = "{}" where date = "{}"'.format(json_entit, time_send))
            connection.commit()
            bot.send_message(message.chat.id, f'<b>Успешно запланировали рассылку <code>{time_send}</code></b>',
                             parse_mode='HTML')


bot.polling(none_stop=True)
