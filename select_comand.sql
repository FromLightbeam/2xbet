cur.execute("select * from Action_money where name ='{0}'".format(action))

cur.execute("select * from users where username ='{0}'".format(username.encode('utf-8')))

cur.execute("select * from Users where  username='{0}' and password='{1}'".format(username, password))

cur.execute("select * from users where id_user ='{0}'".format(user_id))

def get_logs_money(id):
    cur = connection.cursor()
    cur.execute("""select id_money_log,  (select name from Action_money where id_action_money= Money_log.id_action_money) as name,
                            (select username from users where id_user = '{0}') as username,
                            (select id_bet from bet where id_bet= money_log.id_bet) as id_bet,
                            date_time, count from money_log  where id_user='{0}'""".format(id))

def is_admin(user):
      cur.execute("select name from user_group where id_group='{0}'".format(user['group']))

def get_all_users():
  cur.execute("select * from users")

def get_all_logs():
cur.execute("""select logs.id_logs, users.username, action.name, logs.date_time from users, logs, action
                              where logs.user_id = users.id_user and logs.action_id = action.id_action""")

def get_all_club():
  cur.execute("select * from club")

def get_all_match():
      cur.execute("""select id_match, (select name from club where id_club=club_id_1) as club1_name,
                                      (select name from club where id_club=club_id_2) as club2_name,
                                      data, cofficient, goal_1, gola_2, tested from match""")

def get_match_by_id(id):
        cur.execute("select * from match where id_match='{0}'".format(id))

        def get_match_by_id(id):

            cur.execute("select * from match where id_match='{0}'".format(id))

            ans = cur.fetchall()

def get_all_bets(date_min=None, date_max=None, money_min=None, money_max=None):
            cur.execute("""select bet_mutch.id_bet_mutch, id_club, id_match , date_time,
                        (select id_bet from bet where id_bet_mutch=bet_mutch.id_bet_mutch) as id_bet,
                        (select users.username from users where id_user=bet.id_user and bet.id_bet_mutch=bet_mutch.id_bet_mutch),
                        (select id_user from bet where id_bet_mutch=bet_mutch.id_bet_mutch) as id_user,
                        (select count_money from bet where id_bet_mutch=bet_mutch.id_bet_mutch) as money,
                        (select club.name from club, match where id_club=match.club_id_1 and match.id_match=bet_mutch.id_match) as club1,
                        (select club.name from club, match where id_club=match.club_id_2 and match.id_match=bet_mutch.id_match) as club2
                            from bet_mutch, bet where bet_mutch.id_bet_mutch=bet.id_bet_mutch and
                            bet.count_money between '{0}' and '{1}' {2} {3}  """.format(money_min, money_max, date_min, date_max))
