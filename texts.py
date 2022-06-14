import sqlite3

from config import connect

def stata():
	connection,q = connect()
	q.execute(f'SELECT COUNT(id) FROM ugc_spam')
	count_spam = q.fetchone()[0]
	count_white = q.execute(f'SELECT COUNT(id) FROM ugc_white_list')
	count_white = q.fetchone()[0]
	count_userd = q.execute(f'SELECT COUNT(userid) FROM ugc_users')
	count_userd = q.fetchone()[0]
	count_user_vip = q.execute(f'SELECT COUNT(userid) FROM ugc_users where vip ="1"')
	count_user_vip = q.fetchone()[0]

	text = f'''<b>📊 Статистика

👤‍ Пользователей: {count_userd}
💣 Номеров взорвано: {count_spam}</b>'''
	return text



def infa_button():
	text = '''В честь достижения 700 пользователей в нашем бомбере Вашими и Нашими усилиями вышло самое большое обновление в бомбере в котором была добавлена приватная версия бомбера. Если же у вас она имеется вам открываются следующие возможности:

— БОЛЬШЕ СМС В 10РАЗ🌪💣
— СПАМ ЗВОНКОВ ДО 5 В МИНУТУ
— ВОЗМОЖНОСТЬ ДОБАВЛЯТЬ НОМЕР В БЕЛЫЙ ЛИСТ 🗒
— БОЛЬШЕЕ КОЛИЧЕСТВО ВРЕМЕНИ ДЛЯ СПАМА 🔗
— ДОПОЛНИТЕЛЬНЫЕ ПЛЮШКИ И ПРИВАТНЫЕ РОЗЫГРЫШИ ОТ АДМИНА ⚫️
                             
Есть несколько способов получения приватной версии бота:
1. Пригласить 30 пользователей по реферальной ссылке которую можно получить нажав на кнопку "Получить Бесплатно🀀" 
2. Купить доступ нажав на кнопку "▪️Купить доступ▪️" 
3. Участвовать в розыгрышах или  помогать проекту в развитии.'''
	return text

def infa_bomb(phoneid,userid):
	connection,q = connect()
	infa_spam = q.execute(f'SELECT * FROM ugc_spam where id = "{phoneid}"').fetchone()
	text = f'''<b>
❤️ Номер: {infa_spam[2]}
🏳️‍🌈 Страна: {infa_spam[3]}
⏰ Начало спама: {infa_spam[4]}
⏳ Время спама: {infa_spam[5]} мин

📲 Статус: {'😈 Хуярим' if infa_spam[6] == '1' else '👹 Захуярили'}
</b>'''
	return text


def premium_text(userid):
	connection,q = connect()
	infa = q.execute(f'SELECT * FROM ugc_users where userid = "{userid}"').fetchone()
	if str(infa[2]) == '0':
		text = '''<b>Приват🌪

— БОЛЬШЕ СМС В 10РАЗ🌪💣
— ВОЗМОЖНОСТЬ ДОБАВЛЯТЬ НОМЕР В БЕЛЫЙ ЛИСТ 🗒
— БОЛЬШЕЕ КОЛИЧЕСТВО ВРЕМЕНИ ДЛЯ СПАМА 🔗</b>'''
	else:
		text = '''<b>❤️ У вас уже есть премиум доступ, который открывает вам:

— БОЛЬШЕ СМС В 10РАЗ🌪💣
— ВОЗМОЖНОСТЬ ДОБАВЛЯТЬ НОМЕР В БЕЛЫЙ ЛИСТ 🗒
— БОЛЬШЕЕ КОЛИЧЕСТВО ВРЕМЕНИ ДЛЯ СПАМА 🔗</b>'''

	return text

def buy_premium(userid):
	connection,q = connect()
	infa = q.execute(f'SELECT * FROM ugc_config').fetchone()
	text = f'''<b>❗️ Для приобретения доступа к боту переведите 50 рублей на QIWI кошелёк любым способом.

📱 Номер: <code>{infa[1]}</code>
👑 Комментарий: <code>{userid}</code>
💰 Стоимость: <code>50</code> RUB

❗️ Если Вы перевели деньги с другим комментарием, то доступ Вы не получите!</b>'''


	return text


def free_premium(userid):
	connection,q = connect()
	count_userd = q.execute(f'SELECT COUNT(userid) FROM ugc_users where ref = "{userid}"').fetchone()[0]
	if int(count_userd) < 30: 
		text = f'''<b>Для получения приватной версии данного бота - вам нужно пригласить 30 человек по реферальной ссылке🤝.

Ваша реферальная ссылка:
https://t.me/SLFRobot?start={userid}

🤝Приглашено: <code>{count_userd}/30</code></b>'''
	else:
		text = f'''<b>❤️ Вы успешно получили премиум!

Ваша реферальная ссылка:
https://t.me/SLFRobot?start={userid}

🤝Приглашено: <code>{count_userd}/30</code></b>'''
	return text


def white_list():
	text = f'''<b>Список белых номеров\n\nНа номера из этого списка, никто не сможет ставить бомбер</b>'''
	return text




def admin_stata():
	connection,q = connect()
	q.execute(f'SELECT COUNT(userid) FROM ugc_users')
	count_users = q.fetchone()[0]
	q.execute(f'SELECT COUNT(id) FROM ugc_spam')
	count_phone = q.fetchone()[0]
	text = f'''<b>Статистика проекта:
Всего пользователей: {count_users}
Всего уничтожили номеров: {count_phone}</b>'''
	return text