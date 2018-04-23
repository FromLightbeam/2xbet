from django.db import connection


import datetime

def add_log(user_id, action, count):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = connection.cursor()
    cur.execute("select * from Action_money where name ='{0}'".format(action))
    action_id = cur.fetchall()[0][0]
    cur.execute("insert into Money_log(id_action_money, id_user, date_time, count) values('{0}', '{1}', '{2}', '{3}')".format(action_id, user_id, date, count))

def add_log_bet(user_id, action, count, bet):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = connection.cursor()
    cur.execute("select * from Action_money where name ='{0}'".format(action))

    action_id = cur.fetchall()
    print('\n\n\nallah\n\n\n')
    print(type(action_id))
    print(action_id)
    # cur.execute("insert into Money_log(id_action_money, id_user, date_time, count, id_bet) values('{0}', '{1}', '{2}', '{3}', '{4}')".format(action_id, user_id, date, count, bet))
