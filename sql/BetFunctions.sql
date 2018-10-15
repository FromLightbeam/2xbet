CREATE OR REPLACE FUNCTION insert_bet(in_user_id bet.id_user%TYPE, 
                                      in_event_id bet.id_event%TYPE, 
                                      in_money bet.count_money%TYPE) 
RETURN NUMBER
IS
    bet_id bet.id_bet%TYPE;
BEGIN
    INSERT INTO Bet(id_user, id_event, count_money) VALUES(in_user_id, in_event_id, in_money)
    RETURNING id_bet INTO bet_id;
    RETURN bet_id;
END;
/

CREATE OR REPLACE FUNCTION get_users_bet(in_user_id bet.id_user%TYPE)
RETURN SYS_REFCURSOR 
IS
  C SYS_REFCURSOR;
BEGIN

    OPEN C FOR
        SELECT bet.id_bet, match.MATCH_DATE,  club1.name as name_club1, club2.name as name_club2, bet.count_money, event.NAME_EVENT, event.COEFFICIENT  
        FROM bet
        INNER JOIN event
        ON bet.id_event = event.id_event
        INNER JOIN match
        ON event.id_match = match.id_match
        INNER JOIN club club1
        ON match.club_id_1 = club1.id_club
        INNER JOIN club club2
        ON match.club_id_2 = club2.id_club;
    RETURN C;
END;
/

