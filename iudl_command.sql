insert into Action(name) values('log in');
insert into Action(name) values('log out');
insert into Action(name) values('sign up');

insert into Action_money(name) values('add');
insert into Action_money(name) values('withdraw');
insert into Action_money(name) values('win');
insert into Action_money(name) values('lost');

def add_log_bet(user_id, action, count, bet):
      cur.execute("insert into Money_log(id_action_money, id_user, date_time, count, id_bet) values('{0}', '{1}', '{2}', '{3}', '{4}')".format(action_id, user_id, date, count, bet))

def registration(username, name_1, name_2, password, password_confirmation):
          cur.execute('''insert into Users (username, first_name, second_name, password, group_id) values('{0}', '{1}', '{2}', '{3}', '{4}'
                                 )'''.format(username,name_1, name_2, password, 2))

def locks_user_by_id(id):
             cur.execute("update users set is_active = false where id_user='{0}'".format(id))

def add_money(id, money):
        cur.execute("update users set money_count='{0}' where id_user='{1}'".format(money, id))

def withdraw_money(id, money):
            cur.execute("update users set money_count='{0}' where id_user='{1}'".format(money, id))

def create_club(name):
        cur.execute("insert into club(name) values('{0}')".format(name))

def del_club(id):
        cur.execute("delete from club where id_club='{0}'".format(id))

def match_create(id_1, id_2, date, coff):
      cur.execute("insert into match(club_id_1, club_id_2, data, cofficient) values('{0}', '{1}', '{2}', '{3}')".format(int(id_1), int(id_2), date, coff ))

def update_match(id, club1, club2, date, coff, gl1, gl2, test=False):
          cur.execute("""update match
                        set club_id_1='{0}', club_id_2='{1}',
                          data='{2}', cofficient='{3}',
                           goal_1='{4}', gola_2='{5}', tested='{7}' where id_match='{6}'""".format(club1, club2, date, coff, gl1, gl2, id, test))

def match_del(id):
         cur.execute("delete from match where id_match='{0}'".format(id))

def add_game(id_club):
           cur.execute("update club set count_game =count_game+1 where id_club='{0}'".format(id_club))

def add_wingame(id_club):
          cur.execute("update club set win_count_game =win_count_game+1 where id_club='{0}'".format(id_club))

def bet_put(idu, id_m, id_c, money):
              cur.execute("""insert into bet_mutch(id_club, id_match, date_time) values('{0}', '{1}', '{2}')""".format(id_c, id_m, date));
              cur.execute("""insert into bet(id_bet_mutch, id_user, count_money) values('{0}', '{1}', '{2}')""".format(ans[0][0], idu, money));

def add_log(user_id, action):
            cur.execute("insert into Logs(action_id, user_id, date_time) values('{0}', '{1}', '{2}')".format(action_id, user_id, date))
