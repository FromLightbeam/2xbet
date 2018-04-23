drop table logs ;
drop table action;
drop table money_log;
drop table action_money;
drop table bet;
drop table bet_mutch;
drop table users;
drop table user_group;
drop table match;
drop table club;


CREATE TABLE User_group(
  id_group SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(30) NOT NULl
);

CREATE TABLE Users(
  id_user SERIAL NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  second_name VARCHAR(50) NOT NULL,
  password VARCHAR(30) NOT NULL,
  is_active BOOLEAN ,
  money_count INT DEFAULT 0,
  group_id INT NOT NULL,
  username VARCHAR NOT NULL,
  FOREIGN KEY(group_id) REFERENCES User_group(id_group)
);

CREATE TABLE Club(
  id_club SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  count_game INT DEFAULT 0,
  win_count_game INT DEFAULT 0
);

CREATE TABLE Match(
  id_match SERIAL NOT NULL PRIMARY KEY,
  club_id_1 INT NOT NULL,
  club_id_2 INT NOT NULL,
  data DATE NOT NULL,
  caficient decimal DEFAULT 0,
  goal_1 INT,
  gola_2 INT,
  FOREIGN KEY(club_id_1) REFERENCES Club(id_club),
  FOREIGN KEY(club_id_2) REFERENCES Club(id_club)
);

CREATE TABLE Action(
  id_action SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE Logs(
  id_logs SERIAL NOT NULL PRIMARY KEY,
  date_time timestamp,
  action_id INT NOT NULL,
  user_id INT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES Users(id_user),
  FOREIGN KEY(action_id) REFERENCES Action(id_action)
);

CREATE TABLE Action_money(
  id_action_money SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE Bet_mutch(
  id_bet_mutch SERIAL NOT NULL PRIMARY KEY,
  id_club INT NOT NULL,
  id_match INT NOT NULL,
  date_time timestamp,
  FOREIGN KEY(id_club) REFERENCES Club(id_club),
  FOREIGN KEY(id_match) REFERENCES Match(id_match)
);

CREATE TABLE Bet(
  id_bet SERIAL NOT NULL PRIMARY KEY,
  count_money INT NOT NULL,
  id_bet_mutch INT NOT NULL,
  id_user INT NOT NULL,
  FOREIGN KEY(id_bet_mutch) REFERENCES Bet_mutch(id_bet_mutch),
  FOREIGN KEY(id_user) REFERENCES Users(id_user)
);

CREATE TABLE Money_log(
id_money_log SERIAL NOT NULL PRIMARY KEY,
id_action_money INT NOT NULL,
id_user INT NOT NULL,
id_bet INT ,
date_time timestamp,
count INT NOT NULL,
FOREIGN KEY(id_user) REFERENCES Users(id_user),
FOREIGN KEY(id_bet) REFERENCES Bet(id_bet),
FOREIGN KEY(id_action_money) REFERENCES Action_money(id_action_money)
);
