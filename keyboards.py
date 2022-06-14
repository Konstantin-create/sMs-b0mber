import telebot
from telebot import types
import sqlite3
import requests
import json


main_menu = telebot.types.ReplyKeyboardMarkup(True)
main_menu.row('Атака')
main_menu.row('Статистика', 'Информация')

admin = telebot.types.ReplyKeyboardMarkup(True)
admin.row('Статистика проекта')
admin.row('Рассылка')


menu = types.InlineKeyboardMarkup()
menu.add(types.InlineKeyboardButton(text='Бомбить',callback_data=f'бомбим'))
menu.add(types.InlineKeyboardButton(text='Активные',callback_data=f'активные'),types.InlineKeyboardButton(text='История',callback_data=f'история'))
menu.add(types.InlineKeyboardButton(text='PREMIUM доступ',callback_data=f'premium'))


country = types.InlineKeyboardMarkup()
country.add(types.InlineKeyboardButton(text='🇷🇺 Россия',callback_data=f'россия'))
country.add(types.InlineKeyboardButton(text='🇺🇦 Украина',callback_data=f'украина'),types.InlineKeyboardButton(text='🇰🇿 Казахстан',callback_data=f'казахстан'))



def activ_bomber(userid):
	connection = sqlite3.connect('bomber.db')
	q = connection.cursor()
	q = q.execute(f'SELECT * FROM ugc_spam where userid = "{userid}" and status = "1"')
	row = q.fetchall()
	services = types.InlineKeyboardMarkup(row_width=2)
	btns = []
	for i in range(len(row)):
		try:
			btns.append(types.InlineKeyboardButton(text=f'{row[i][2]}',callback_data=f'аинфа_{row[i][0]}'))		
		except:
			continue
	while btns != []:
		try:
			services.add(
				btns[0],
				btns[1],
				)
			del btns[1], btns[0]
		except:
			services.add(btns[0])
			del btns[0]
	services.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	return services


def all_bomber(userid):
	connection = sqlite3.connect('bomber.db')
	q = connection.cursor()
	q = q.execute(f'SELECT * FROM ugc_spam where userid = "{userid}"')
	row = q.fetchall()
	services = types.InlineKeyboardMarkup(row_width=3)
	btns = []
	for i in range(len(row)):
		try:
			btns.append(types.InlineKeyboardButton(text=f'{row[i][2]}',callback_data=f'винфа_{row[i][0]}'))		
		except:
			continue
	while btns != []:
		try:
			services.add(
				btns[0],
				btns[1],
				btns[2]
				)
			del btns[2],btns[1], btns[0]
		except:
			services.add(btns[0])
			del btns[0]
	services.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	return services



def premium(userid):
	connection = sqlite3.connect('bomber.db')
	q = connection.cursor()
	infa = q.execute(f'SELECT * FROM ugc_users where userid = "{userid}"').fetchone()
	if str(infa[2]) == '0':
		menu = types.InlineKeyboardMarkup()
		menu.add(types.InlineKeyboardButton(text='Получить',callback_data=f'получить_прем'))
		menu.add(types.InlineKeyboardButton(text='Купить',callback_data=f'купить_прем'))
		menu.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	else:
		menu = types.InlineKeyboardMarkup()
		menu.add(types.InlineKeyboardButton(text='White list',callback_data=f'white_list'))
		menu.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	return menu


def buy_premium(userid):
	connection = sqlite3.connect('bomber.db')
	q = connection.cursor()
	infa = q.execute(f'SELECT * FROM ugc_config').fetchone()
	menu = types.InlineKeyboardMarkup()
	url = f'https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={infa[1]}&amountFraction=0&extra%5B%27comment%27%5D={userid}&currency=643&blocked[0]=account'
	menu.add(types.InlineKeyboardButton(text='Оплатить',url=url))
	menu.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	return menu



def white_list(userid):
	connection = sqlite3.connect('bomber.db')
	q = connection.cursor()
	q = q.execute(f'SELECT * FROM ugc_white_list where userid = "{userid}"')
	row = q.fetchall()
	services = types.InlineKeyboardMarkup(row_width=3)
	btns = []
	for i in range(len(row)):
		try:
			btns.append(types.InlineKeyboardButton(text=f'{row[i][2]}',callback_data=f'линфа_{row[i][2]}'))		
		except:
			continue
	while btns != []:
		try:
			services.add(
				btns[0],
				btns[1],
				btns[2]
				)
			del btns[2],btns[1], btns[0]
		except:
			services.add(btns[0])
			del btns[0]
	services.add(types.InlineKeyboardButton(text='Добавить номер',callback_data=f'добавить_номер'))
	services.add(types.InlineKeyboardButton(text='Назад',callback_data=f'вернуться_главная'))
	return services









