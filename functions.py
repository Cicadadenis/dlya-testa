import sqlite3
import os
import random
import requests
import json
import datetime
import threading
import traceback
from time import time
from datetime import datetime, date
from sys import exit
from random import choice
start_date = '04.07.2021'




lock = threading.Lock()
conn = sqlite3.connect('base.db', check_same_thread=False)
cur = conn.cursor()

def first_join(user_id, name):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"').fetchall()
    
    if len(row) == 0:
        cursor.execute(f'INSERT INTO users VALUES ("{user_id}", "{name}", "{date.today()}", "0", "0", "0", "0", "0", "0", "0", "0")')
        conn.commit()
    
    row2 = cursor.execute(f'SELECT * FROM sett WHERE user_id = "{user_id}"').fetchall()
    if len(row2) == 0:
        cursor.execute(f'INSERT INTO sett VALUES ("{user_id}", "8", "y", "y", "y", "y")')
        conn.commit()
        
def count_ref(user_id, name, code):
	lock.acquire(True)

	cur.execute('SELECT count FROM reffers WHERE user_id = ?', (code,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute(f'INSERT INTO reffers VALUES ("{code}", "{name}", "0")')
		return 0

	return link[0]
        
def reffer(user_id, name, code):
	current = count_ref(user_id, name, code)
	conn = sqlite3.connect('base.db')
	cursor = conn.cursor()
	row = cursor.execute(f'SELECT * FROM reffers WHERE user_id = "{code}"').fetchall()

	ref_code = code
	if ref_code == '':
		ref_code = 0
    
	cursor.execute(f'UPDATE reffers SET count = ? WHERE user_id = ?', (current+1, code))
	conn.commit()

	return True, ref_code
        
	return False, 0
        
def users_info():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users').fetchone()

    current_time = str(datetime.now())

    amount_user_all = 0
    amount_user_day = 0
    amount_user_hour = 0

    while row is not None:
        amount_user_all += 1
        if row[2][:-15:] == current_time[:-15:]:
            amount_user_day += 1
        if row[2][:-13:] == current_time[:-13:]:
            amount_user_hour += 1

        row = cursor.fetchone()

    msg = f"""
?????????????<b>?????????? ????????</b>: <code>{start_date}</code>s
???? <b>??????????????????????????</b>: <code>{amount_user_all}</code>
"""

    return msg

def admin_info():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users').fetchone()

    current_time = str(datetime.datetime.now())

    amount_user_all = 0
    amount_user_day = 0
    amount_user_hour = 0

    while row is not None:
        amount_user_all += 1
        if row[2][:-15:] == current_time[:-15:]:
            amount_user_day += 1
        if row[2][:-13:] == current_time[:-13:]:
            amount_user_hour += 1

        row = cursor.fetchone()

    msg = f"""
??? ?????????????????? ?? ??????????????????????????:

??? ???? ?????? ?????????? - {amount_user_all}
??? ???? ???????? - {amount_user_day}
??? ???? ?????? - {amount_user_hour}
"""

    return msg


def ban():
    conn = sqlite3.connect('ban.db')
    cursor = conn.cursor()

    ls = cursor.execute(f'SELECT * FROM list').fetchall()
    ls2 = []

    for i in ls:
        ls2.append(i[0])
    return ls2
    




def get_count_link(user_id):
	lock.acquire(True)

	cur.execute('SELECT short FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users(short) WHERE user_id(?) VALUES(?)', (0, user_id,))
		return 0

	return link[0]    
def act_count_link(act, user_id):
	current = get_count_link(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET short = ? WHERE user_id = ?', (current+1, user_id))

	conn.commit()

	lock.release()




def get_count_deanon(user_id):
	lock.acquire(True)

	cur.execute('SELECT deanon FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users (deanon) VALUES(?) WHERE user_id(?)', (0, user_id,))
		return 0

	return link[0]

def act_count_deanon(act, user_id):
	current = get_count_deanon(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET deanon = ? WHERE user_id = ?', (current+1, user_id))

	conn.commit()

	lock.release()





def get_count_name(user_id):
	lock.acquire(True)

	cur.execute('SELECT gen_name FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users (gen_name) VALUES(?) WHERE user_id(?)', (0, user_id,))
		return 0

	return link[0]

def act_count_name(act, user_id):
	current = get_count_name(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET gen_name = ? WHERE user_id = ?', (current+1, user_id))
	if act.lower() == 'add5':
		cur.execute('UPDATE users SET gen_name = ? WHERE user_id = ?', (current+5, user_id))

	conn.commit()

	lock.release()


def get_count_ip(user_id):
	lock.acquire(True)

	cur.execute('SELECT ip FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users (ip) VALUES(?) WHERE user_id(?)', (0, user_id,))
		return 0

	return link[0]

def act_count_ip(act, user_id):
	current = get_count_name(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET ip = ? WHERE user_id = ?', (current+1, user_id))

	conn.commit()

	lock.release()



def get_count_proxies(user_id):
	lock.acquire(True)

	cur.execute('SELECT proxies FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users(proxies) VALUES(?)', (0,))
		return 0

	return link[0]

def act_count_proxies(act, user_id):
	current = get_count_name(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET proxies = ? WHERE user_id = ?', (current+7, user_id))

	conn.commit()

	lock.release()


def get_count_tg_id(user_id):
	lock.acquire(True)

	cur.execute('SELECT tg_id FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users (tg_id) VALUES(?) WHERE user_id(?)', (0, user_id,))
		return 0

	return link[0]

def act_count_tg_id(act, user_id):
	current = get_count_name(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET tg_id = ? WHERE user_id = ?', (current+1, user_id))

	conn.commit()

	lock.release()

def get_count_screen(user_id):
	lock.acquire(True)

	cur.execute('SELECT screen FROM users WHERE user_id = ?', (user_id,))
	link = cur.fetchone()

	lock.release()

	if not link:
		cur.execute('INSERT INTO users (screen) VALUES(?) WHERE user_id(?)', (0, user_id,))
		return 0
    
	if len(link) == 'Null' or 'None' or 'NoneTypes' or 'NoneType':
		cur.execute('INSERT INTO users (screen) VALUES(?)', (0,))
    
	return link[0]

def act_count_screen(act, user_id):
	current = get_count_screen(user_id)

	lock.acquire(True)

	if act.lower() == 'add':
		cur.execute('UPDATE users SET screen = ? WHERE user_id = ?', (current+1, user_id))

	conn.commit()

	lock.release()


def stata(qq):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    b = cursor.execute(f'SELECT SUM(deanon) FROM users').fetchone()
    b1 = cursor.execute(f'SELECT SUM(short) FROM users').fetchone()
    b2 = cursor.execute(f'SELECT SUM(gen_name) FROM users').fetchone()
    b3 = cursor.execute(f'SELECT SUM(ip) FROM users').fetchone()
    b4 = cursor.execute(f'SELECT SUM(proxies) FROM users').fetchone()
    b5 = cursor.execute(f'SELECT SUM(tg_id) FROM users').fetchone()
    ban = cursor.execute(f'SELECT user_id from ban').fetchone()
    
    
    row = cursor.execute(f'SELECT * FROM users').fetchone()
    current_time = str(datetime.now())
    cur_time = date.today()

    amount_user_all = 0
    amount_user_day = 0
    amount_user_hour = 0

    while row is not None:
        amount_user_all += 1
        if row[2][:-15:] == current_time[:-15:]:
            amount_user_day += 1
        if row[2][:-13:] == current_time[:-13:]:
            amount_user_hour += 1

        row = cursor.fetchone()
        
    
    msg = f'''???????????????? ??????????!
???? <b>?????? ???????????????????? ???? {cur_time}</b>:

???? <b>??????????????????????????:</b> <code>{amount_user_all}</code>
???? <b>?????????????????????????? ?? ????????:</b> <code>{ban[0]}</code>
?????? <b>???????????? ??????????????????</b>: <code>{b1[0]}</code>
???? <b>?????????????? ??????????????:</b> <code>{b[0]}</code>
???? <b>?????????? ??????????????????????????:</b> <code>{b2[0]}</code>
???? <b>IP ??????????????</b>: <code>{b3[0]}</code>
???? <b>TG ???????????? ??????????????</b>: <code>{b5[0]}</code>
???? <b>???????????? ??????????????????????????</b>: <code>{b4[0]}</code>
?????? <b>???????????? ????????????????????</b> <code>{qq}</code>'''

    return msg
    
        
    
