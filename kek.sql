--drop table logs ;
--drop table action;
--drop table money_log;
--drop table action_money;
--drop table bet;
--drop table bet_mutch;
--drop table users;
--drop table user_group;
drop table Match;
drop table Club;




CREATE TABLE Club(
  id_club  NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  CONSTRAINT pk_club PRIMARY KEY (id_club),
  name VARCHAR(150) NOT NULL,
  count_game INT DEFAULT 0,
  win_count_game INT DEFAULT 0
);

CREATE TABLE Match(
  id_match NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  club_id_1 INT NOT NULL,
  club_id_2 INT NOT NULL,
  data DATE NOT NULL,
  coefficient decimal DEFAULT 0,
  goal_1 INT,
  gola_2 INT,
  CONSTRAINT club_pk_1
    FOREIGN KEY(club_id_1) 
    REFERENCES Club(id_club),
  CONSTRAINT club_pk_2
    FOREIGN KEY(club_id_2) 
    REFERENCES Club(id_club)
);

CREATE TABLE User_group(
  id_group NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  name VARCHAR(30) NOT NULL
);

CREATE TABLE Users(
  id_user NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
  first_name VARCHAR(50) NOT NULL,
  second_name VARCHAR(50) NOT NULL,
  password VARCHAR(30) NOT NULL,
  is_active BO,
  money_count INT DEFAULT 0,
  group_id INT NOT NULL,
  username VARCHAR NOT NULL,
  CONSTRAINT group_pk
    FOREIGN KEY(group_id) 
    REFERENCES User_group(id_group)
);

