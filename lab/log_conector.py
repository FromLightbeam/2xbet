from django.db import connection

import datetime

def add_log(user_id, action):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = connection.cursor()
    cur.execute("select * from Action where name ='{0}'".format(action))
    action_id = cur.fetchall()[0][0]
    cur.execute("insert into Logs(action_id, user_id, date_time) values('{0}', '{1}', '{2}')".format(action_id, user_id, date))
