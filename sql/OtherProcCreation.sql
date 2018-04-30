CREATE OR REPLACE PROCEDURE insert_user(username2 IN VARCHAR, first__name IN VARCHAR, 
                                        second__name IN VARCHAR, password2 IN VARCHAR, group__id IN INT)
IS
BEGIN
  insert into Users (username, first_name, second_name, password, group_id) 
  values(username2, first__name, second__name, password2, group__id);
END;
/

CREATE OR REPLACE FUNCTION count_user(in_username IN users.username%TYPE) 
return NUMBER 
is
  num NUMBER;
BEGIN
    SELECT COUNT(*) INTO num FROM users WHERE username=in_username;
    RETURN num;
END;
/


CREATE OR REPLACE FUNCTION get_user(in_username IN users.username%TYPE, in_password IN users.password%TYPE) 
--RETURN users%ROWTYPE
--IS
--  rec users%ROWTYPE;
return SYS_REFCURSOR is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT * FROM users WHERE username=in_username AND password=in_password;
    RETURN C;
END;
/

CREATE OR REPLACE FUNCTION get_user_by_id(in_user IN USERS.ID_USER%TYPE) 
--RETURN users%ROWTYPE
--IS
--  rec users%ROWTYPE;
return SYS_REFCURSOR is
  C SYS_REFCURSOR;
BEGIN
    OPEN C FOR
    SELECT * FROM users WHERE id_user=in_user;
    RETURN C;
END;
/

CREATE OR REPLACE FUNCTION is_admin(in_username IN users.username%TYPE) 
return NUMBER
is
  num NUMBER;
BEGIN
    SELECT COUNT(*) INTO num FROM users WHERE username=in_username AND group_id=1;
    return num;
--    IF num > 0 THEN
--        RETURN TRUE;
--    ELSE
--        RETURN FALSE;
--    END IF;
END;
/



