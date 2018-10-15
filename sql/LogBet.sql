DROP TABLE bet_log;

CREATE TABLE bet_log (
    id_bet_log INT GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
    action_type VARCHAR(10),
    action_date DATE,
    row_id INT,
    
    old_count_money INT,
    old_id_event VARCHAR(20),
    old_id_user INT,
    
    new_count_money INT,
    new_id_event VARCHAR(20),
    new_id_user INT
);

CREATE OR REPLACE TRIGGER log_bet
BEFORE INSERT OR UPDATE OR DELETE
ON bet
FOR EACH ROW
DECLARE
    PRAGMA AUTONOMOUS_TRANSACTION;
    action_type bet_log.action_type%type;
    id bet_log.row_id%type;
BEGIN
    IF INSERTING THEN
        action_type := 'Insert';
        id := :NEW.id_bet;
    ELSIF UPDATING THEN
        action_type := 'Update';
        id := :NEW.id_bet;
    ELSIF DELETING THEN
        action_type := 'Delete';
        id := :OLD.id_bet;
    END IF;

    INSERT INTO bet_log (action_type, action_date, row_id, 
                                     old_count_money, old_id_event, old_id_user, 
                                     new_count_money, new_id_event, new_id_user)
        VALUES (action_type, SYSDATE, id, 
                :OLD.count_money, :OLD.id_event, :OLD.id_user, 
                :NEW.count_money, :NEW.id_event, :NEW.id_user);
    COMMIT;
END;
/