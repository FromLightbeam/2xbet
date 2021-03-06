from django.db import connection

from lab.helper import fetch_one_dict_from_cursor, fetch_many_dict_from_cursor

import acaunt.user_db_conect as user_db_conect
import cx_Oracle

def is_admin(user):
    cur = connection.cursor()

    is_admin = cur.callfunc('is_admin', cx_Oracle.NUMBER, [user['username'], ])

    if is_admin > 0:
        return True
    else:
        return False


def get_all_users():
    cur = connection.cursor()
    cur.execute("select * from users")
    ans = cur.fetchall()
    ans_1 = list()
    for item in ans:
        ans_1.append(user_db_conect.make_user(item))
    return ans_1

def get_all_logs():
    cur = connection.cursor()
    cur.execute("""select logs.id_logs, users.username, action.name, logs.date_time from users, logs, action
                            where logs.user_id = users.id_user and logs.action_id = action.id_action""")
    ans = cur.fetchall()
    return ans

def get_all_club():
    cur = connection.cursor()
    cur.execute("select * from club")
    ans = cur.fetchall()
    return ans

def create_club(name):
    cur = connection.cursor()
    cur.execute("insert into club(name) values('{0}')".format(name))
    return True

def del_club(id):
    cur = connection.cursor()
    cur.execute("delete from club where id_club='{0}'".format(id))
    return True


################################ MATCH #########################################

def match_create(id_1, id_2, date):
    cur = connection.cursor()
    cur.callproc("insert_match", [ int(id_1), int(id_2), date, ])
    return True

def get_all_match():
    cur = connection.cursor()
    ans = cur.callfunc('get_all_match', cx_Oracle.CURSOR, [])
    return fetch_many_dict_from_cursor(ans)

def get_match_by_id(id_match):
    cur = connection.cursor()
    ans = cur.callfunc('get_match_by_id', cx_Oracle.CURSOR, [id_match, ])
    return fetch_one_dict_from_cursor(ans)

def update_match(id, club1, club2, date, goal1, goal2):
    cur = connection.cursor()
    cur.callproc("update_match", [club1, club2, date, goal1, goal2, id, ])
    return True

def match_del(id):
    cur = connection.cursor()
    cur.execute("delete from match where id_match='{0}'".format(id))
    return True

################################################################################

def get_event(id_match):
    cur = connection.cursor()

    ans = cur.callfunc('get_events_by_match_id', cx_Oracle.CURSOR, [id_match, ])
    return fetch_many_dict_from_cursor(ans)


def get_events(matches):
    cur = connection.cursor()
    for match in matches:
        ans = cur.callfunc('get_events_by_match_id', cx_Oracle.CURSOR, [match['id_match'], ])
        match['events'] = fetch_many_dict_from_cursor(ans)

    return matches

def add_events(id_match, events):
    cur = connection.cursor()

    for event, coeff in events.items():
        cur.callproc('insert_event', [event, coeff, id_match])


def del_events(id_match):
    cur = connection.cursor()

    cur.callproc('delete_events', [id_match, ])


def get_bet_mtach_by_id_match(id, id_w):
    cur = connection.cursor()
    cur.execute("select * from bet_match where id_match='{0}' and id_club='{1}'".format(id, id_w))
    ans = cur.fetchall()
    return ans

def get_bet_by_id_btm(id):
    cur = connection.cursor()
    cur.execute("select * from bet where id_bet_match='{0}'".format(id))
    ans = cur.fetchall()
    return ans[0]

def add_game(id_club):
    cur = connection.cursor()
    cur.execute("update club set count_game =count_game+1 where id_club='{0}'".format(id_club))
    return True

def add_wingame(id_club):
    cur = connection.cursor()
    cur.execute("update club set win_count_game =win_count_game+1 where id_club='{0}'".format(id_club))
    return True

def get_all_bets(date_min=None, date_max=None, money_min=None, money_max=None):
    cur = connection.cursor()
    if money_min == None:
        money_min = 0
    if money_max == None:
        money_max = 2147483647
    if date_min != None:
        date_min = "and date_time >= '{0}' ".format(date_min)
    else:
        date_min = ""
    if date_max != None:
        date_max = " and date_time <= '{0} 23:59:59'".format(date_max)
    else:
        date_max = ""
    # shit shit shit
    # cur.execute("""select bet_match.id_bet_match, id_club, id_match , date_time,
    #             (select id_bet from bet where id_bet_match=bet_match.id_bet_match) as id_bet,
    #             (select users.username from users where id_user=bet.id_user and bet.id_bet_match=bet_match.id_bet_match),
    #             (select id_user from bet where id_bet_match=bet_match.id_bet_match) as id_user,
    #             (select count_money from bet where id_bet_match=bet_match.id_bet_match) as money,
    #             (select club.name from club, match where id_club=match.club_id_1 and match.id_match=bet_match.id_match) as club1,
    #             (select club.name from club, match where id_club=match.club_id_2 and match.id_match=bet_match.id_match) as club2
    #                 from bet_match, bet where bet_match.id_bet_match=bet.id_bet_match and
    #                 bet.count_money between '{0}' and '{1}' {2} {3}  """.format(money_min, money_max, date_min, date_max))
    # ans = cur.fetchall()
    # return ans
    return []

def create_new_db():
    cur = connection.cursor()
    