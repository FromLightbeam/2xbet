CREATE OR REPLACE PROCEDURE insert_event(in_name_event event.name_event%TYPE, 
                                         in_coeff event.coefficient%TYPE, 
                                         in_id_match event.id_match%TYPE)
IS
BEGIN
    INSERT INTO event(name_event, coefficient, id_match) 
    VALUES(in_name_event, in_coeff, in_id_match);
END;
/

CREATE OR REPLACE FUNCTION get_events_by_match_id(in_id_match match.id_match%TYPE) 
return SYS_REFCURSOR is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT name_event, coefficient FROM event WHERE id_match = in_id_match;
    RETURN C;
END;
/



CREATE OR REPLACE PROCEDURE delete_events(in_id_match match.id_match%TYPE) 
IS
BEGIN
    DELETE FROM event WHERE id_match=in_id_match;
END;
/