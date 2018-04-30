from django.db import connection

import cx_Oracle
import datetime

from lab.helper import fetch_one_dict_from_cursor

def get_match_by_id_rate(id_match):
    cur = connection.cursor()
    ans = cur.callfunc('get_match_by_id_rate', cx_Oracle.CURSOR, [id_match, ])
    return fetch_one_dict_from_cursor(ans)

def bet_put(user_id, event_id, money):
    cur = connection.cursor()
    bet_id = cur.callfunc('insert_bet', cx_Oracle.NUMBER, [user_id, event_id, money, ])    
    return bet_id
