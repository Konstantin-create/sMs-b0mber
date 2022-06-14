import requests
import json
from user_agent import generate_user_agent
import time
import datetime
import threading
import random
from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent
import bomber
from config import connect


def spam_ru(phone,colvo_time,date_start, userid):
	connection,q = connect()
	q.execute(f'SELECT * FROM ugc_spam where phone = "{phone}" and status = "1" and date_start = "{colvo_time}"')
	row = q.fetchone()
	print(row)
	if row != None:
		while True:
			now = datetime.datetime.now()
			today = str(now)
			print(str(today[:16]), str(row[4]))
			if str(today[:16]) == str(row[4]):
				deadline = int(row[5]) * 60
				colvo_timee = float(deadline) +  time.time()
				if time.time() <= float(colvo_timee):
				# while time.monotonic() < deadline:
					for i in range(1):
						asdasd3 = threading.Thread(target=bomber.main, args=(phone,colvo_timee, userid)).start()
				break
			else:
				time.sleep(5)
