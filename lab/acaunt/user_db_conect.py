from django.db import connection

from lab.helper import fetch_many_dict_from_cursor, fetch_one_dict_from_cursor

import cx_Oracle


def make_user(arg):
    argv = dict()
    argv['id'] = arg[0]
    argv['username'] = arg[7]
    argv['first_name'] = arg[1]
    argv['last_name'] = arg[2]
    argv['is_activ'] = arg[4]
    argv['money'] = arg[5]
    argv['group'] = arg[6]
    return argv

def exist_user(username):
    cur = connection.cursor()
    count = cur.callfunc('count_user', cx_Oracle.NUMBER, [username,])
    if (count > 0):
        return True
    else:
        return False

def registration(username, name_1, name_2, password, password_confirmation):
    
    cur = connection.cursor()

    cur.callproc('insert_user', [username, name_1, name_2, password, 2])
    r = cur.callfunc('get_user', cx_Oracle.CURSOR, [username, password])

    return make_user(r.fetchall()[0])


def authenticate(username, password):
    try:
        cur = connection.cursor()
        r = cur.callfunc('get_user', cx_Oracle.CURSOR, [username, password])
        fetchall = r.fetchall()
        if len(fetchall) != 0:
            return make_user(fetchall[0])
    except:
        return False

def get_user_by_id(user_id):
    cur = connection.cursor()
    res = cur.callfunc('get_user_by_id', cx_Oracle.CURSOR, [user_id,])
    fetchall = res.fetchall()
    if len(fetchall) != 0:
        return make_user(fetchall[0])
    return False


def get_user(username):
    cur = connection.cursor()
    cur.execute("select * from users where username='{0}'".format(username))
    fetchall = cur.fetchall()
    if len(fetchall) != 0:
        return make_user(fetchall[0])
    return False

def del_user_by_id(id):
    cur = connection.cursor()
    cur.execute("delete from users where id_user='{0}'".format(id))
    return True

def locks_user_by_id(id):
    cur = connection.cursor()
    cur.execute("update users set is_active = false where id_user='{0}'".format(id))
    return True

def unlocks_user_by_id(id):
    cur = connection.cursor()
    cur.execute("update users set is_active = true where id_user='{0}'".format(id))
    return True


def add_money(id, money):
    user = get_user_by_id(id)
    money = user['money'] + money
    cur = connection.cursor()
    try:
        cur.execute("update users set money_count='{0}' where id_user='{1}'".format(money, id))
        return money
    except:
        return False

def withdraw_money(id, money):
    user = get_user_by_id(id)
    money = user['money'] - money
    if money < 0:
        return False
    else:
        cur = connection.cursor()
        try:
            cur.execute("update users set money_count='{0}' where id_user='{1}'".format(money, id))
            return money
        except:
            return False
'''
cur.execute("""select Money_log.id_money_log, Action_money.name, Users.username, bet.id_bet, date_time, count
                            from money_log, users, Action_money, bet where
                            Money_log.id_user = '{0}' and money_log.id_action_money=Action_money.id_action_money and
                            money_log.id_bet=bet.id_bet """.format(id))'''

def get_logs_money(id):
    cur = connection.cursor()
    cur.execute("""select id_money_log,  (select name from Action_money where id_action_money= Money_log.id_action_money) as name,
                            (select username from users where id_user = '{0}') as username,
                            (select id_bet from bet where id_bet= money_log.id_bet) as id_bet,
                            date_time, count from money_log  where id_user='{0}'""".format(id))

    ans = cur.fetchall()
    return ans

def get_users_bet(id):
    #   match date money event coefficient 
    cur = connection.cursor()
    ans = cur.callfunc('get_users_bet', cx_Oracle.CURSOR, [id, ])
    # print(ans)
    result = fetch_many_dict_from_cursor(ans)
    print(result)
    return result
