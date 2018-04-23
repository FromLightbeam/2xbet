from django.db import connection
import datetime

def get_match_by_id_rate(id):
    cur = connection.cursor()
    cur.execute("select id_match, (select name from club where id_club = club_id_1)as cl1,"
                "(select name from club where id_club = club_id_2)as cl2, data, coefficient, "
                "club_id_1, club_id_2 " #here was tested
                "from match where id_match = {0}".format(id));
    ans = cur.fetchall()
    return ans

def bet_put(idu, id_m, id_c, money):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = connection.cursor()
    cur.execute("""insert into bet_match(id_club, id_match, date_time) values('{0}', '{1}', '{2}')""".format(id_c, id_m, date));
    cur.execute("select id_bet_match from bet_match where date_time='{0}'".format(date))
    ans = cur.fetchall()
    print (ans)
    cur.execute("""insert into bet(id_bet_match, id_user, count_money) values('{0}', '{1}', '{2}')""".format(ans[0][0], idu, money));
    cur.execute("select id_bet from bet where id_bet_match='{0}'".format(ans[0][0]))
    ans = cur.fetchall()
    return ans[0][0]
