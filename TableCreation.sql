drop table logs ;
drop table action;
drop table money_log;
drop table action_money;
drop table bet;
drop table bet_match;
drop table users;
drop table user_group;
drop table Match;
drop table Club;


CREATE TABLE Club(
  id_club INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_club PRIMARY KEY (id_club),
  name VARCHAR(150) NOT NULL,
  count_game INT DEFAULT 0,
  win_count_game INT DEFAULT 0
);

CREATE TABLE Match(
  id_match INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_match PRIMARY KEY (id_match),
  club_id_1 INT NOT NULL,
  club_id_2 INT NOT NULL,
  data DATE NOT NULL,
  coefficient decimal DEFAULT 0,
  goal_1 INT,
  goal_2 INT,
  CONSTRAINT club_pk_1
    FOREIGN KEY(club_id_1) 
    REFERENCES Club(id_club),
  CONSTRAINT club_pk_2
    FOREIGN KEY(club_id_2) 
    REFERENCES Club(id_club)
);

CREATE TABLE User_group(
  id_group INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_group PRIMARY KEY (id_group),
  name VARCHAR(30) NOT NULL
);

CREATE TABLE Users(
  id_user INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_user PRIMARY KEY (id_user),
  first_name VARCHAR(50) NOT NULL,
  second_name VARCHAR(50) NOT NULL,
  password VARCHAR(30) NOT NULL,
  
  is_active NUMBER,
  money_count NUMBER DEFAULT 0,
  group_id INT NOT NULL,
  username VARCHAR(20) NOT NULL,
  CONSTRAINT group_pk
    FOREIGN KEY(group_id) 
    REFERENCES User_group(id_group)
);


CREATE TABLE Action(
  id_action INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_action PRIMARY KEY (id_action),
  name VARCHAR(100)
);

CREATE TABLE Logs(
  id_logs INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_logs PRIMARY KEY (id_logs),
  date_time timestamp,
  action_id INT NOT NULL,
  user_id INT NOT NULL,
  CONSTRAINT user_pk
    FOREIGN KEY(user_id) REFERENCES Users(id_user),
  CONSTRAINT action_pk
    FOREIGN KEY(action_id) REFERENCES Action(id_action)
);

CREATE TABLE Action_money(
  id_action_money INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_action_money PRIMARY KEY (id_action_money),
  name VARCHAR(100) NOT NULL
);

CREATE TABLE Bet_match(
  id_bet_match INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_bet_match PRIMARY KEY (id_bet_match),
  id_club INT NOT NULL,
  id_match INT NOT NULL,
  date_time timestamp,
  CONSTRAINT pk_club_bet
    FOREIGN KEY(id_club) REFERENCES Club(id_club),
  CONSTRAINT pk_match_bet
    FOREIGN KEY(id_match) REFERENCES Match(id_match)
);

CREATE TABLE Bet(
  id_bet INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_bet PRIMARY KEY (id_bet),
  count_money INT NOT NULL,
  id_bet_match INT NOT NULL,
  id_user INT NOT NULL,
  CONSTRAINT pk_bet_match_bet
    FOREIGN KEY(id_bet_match) REFERENCES Bet_match(id_bet_match),
  CONSTRAINT pk_user_bet
    FOREIGN KEY(id_user) REFERENCES Users(id_user)
);


CREATE TABLE Money_log(
  id_money_log INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_money_log PRIMARY KEY (id_money_log),
  id_action_money INT NOT NULL,
  id_user INT NOT NULL,
  id_bet INT,
  date_time timestamp,
  count INT NOT NULL,
  CONSTRAINT pk_id_user_money_log
    FOREIGN KEY(id_user) REFERENCES Users(id_user),
  CONSTRAINT pk_bet_money_log
    FOREIGN KEY(id_bet) REFERENCES Bet(id_bet),
  CONSTRAINT pk_action_money_money_log
    FOREIGN KEY(id_action_money) REFERENCES Action_money(id_action_money)
);


DECLARE
    num INTEGER;
BEGIN
  insert into User_group (name) values('first');
  insert into User_group (name) values('second');

--  insert into Users (username, first_name, second_name, password, group_id) values('1', '1', '1', '1', 2);
  insert into Action(name) values('log in');
  insert into Action(name) values('log out');
  insert into Action(name) values('sign up');

  insert into Action_money(name) values('add'); 
  insert into Action_money(name) values('withdraw');
  insert into Action_money(name) values('win');
  insert into Action_money(name) values('lost');
  insert into Users (username, first_name, second_name, password, group_id) values('admin', 'kek', 'lol', '123', 1);
--   insert into Users (username, first_name, second_name, password, group_id) values('1', '1', '1', '1', 2);

END;