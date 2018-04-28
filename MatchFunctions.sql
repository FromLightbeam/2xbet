CREATE OR REPLACE FUNCTION get_match_by_id_rate(in_id_match match.id_match%TYPE) 
return SYS_REFCURSOR is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT id_match,
           (SELECT name FROM club WHERE id_club = club_id_1) as name_club1,
           (SELECT name FROM club WHERE id_club = club_id_2) as name_club2, 
           match_date, club_id_1, club_id_2
           FROM  match WHERE id_match = in_id_match;
    RETURN C;
END;
/

CREATE OR REPLACE FUNCTION get_match_by_id(in_id_match match.id_match%TYPE) 
return SYS_REFCURSOR is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT * FROM  match WHERE id_match = in_id_match;
    RETURN C;
END;
/

CREATE OR REPLACE FUNCTION get_all_match RETURN SYS_REFCURSOR 
is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT id_match, 
           (SELECT name FROM club WHERE id_club = club_id_1) as name_club1,
           (SELECT name FROM club WHERE id_club = club_id_2) as name_club2, 
           match_date, goal_1, goal_2 FROM match;
    RETURN C;
END;
/

CREATE OR REPLACE PROCEDURE insert_match(in_club_id_1 club.id_club%TYPE, 
                                         in_club_id_2 club.id_club%TYPE, 
                                         in_match_date match.match_date%TYPE)
IS
BEGIN
    INSERT INTO match(club_id_1, club_id_2, match_date) 
    VALUES(in_club_id_1, in_club_id_2, in_match_date);
END;
/

CREATE OR REPLACE PROCEDURE update_match(in_club1 club.id_club%TYPE, 
                                         in_club2 club.id_club%TYPE, 
                                         in_date match.match_date%TYPE, 
                                         in_goal1 match.goal_1%TYPE,
                                         in_goal2 match.goal_2%TYPE, 
                                         in_id match.id_match%TYPE)
IS
BEGIN
    UPDATE match
    SET club_id_1 = in_club1,
        club_id_2 = in_club2,
        match_date = in_date,
        goal_1 = in_goal1,
        goal_2 = in_goal2  
    WHERE id_match = in_id;
END;
/
