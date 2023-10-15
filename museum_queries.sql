/*1) Show all tables and explain how they are related to one another (keys, triggers, etc.)*/

SHOW TABLES;   /*Shows a list of table names*/

SELECT *
FROM ARTIST;   /*Shows full ARTIST table with data if required. Can replace ARTIST with each table name found in the previous query to display each individual table.*/

SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'ARTMUSEUM' AND REFERENCED_TABLE_NAME IS NOT NULL;   /*Shows primary and foreign key relationships between tables*/

/* As shown by the results of the query above, ART_OBJECT references the AName attribute from the ARTIST table (with the Artist attribute) and the EName attribute from the EXHIBITIONS table (with the Exhibition attribute).
The BORROWED table references the Id_no attribute from the ART_OBJECT table and the CName attribute from the COLLECTIONS table (with the Collection attribute).
The OTHER, PAINTING, PERMANENT_COLLECTION, and SCULPTURE tables all reference the Id_no attribute from the ART_OBJECT table.*/


/*2) A basic retrieval query*/

SELECT A.Id_no, A.Title
FROM ART_OBJECT AS A, PAINTING AS P
WHERE A.Id_no = P.Id_no;


/*3) A retrieval query with ordered results*/

SELECT A.Id_no, A.Title, P.Cost
FROM ART_OBJECT AS A, PERMANENT_COLLECTION AS P
WHERE A.Id_no = P.Id_no
ORDER BY P.Cost ASC;


/*4) A nested retrieval query*/

SELECT A.AName, B.Title
FROM ARTIST AS A, ART_OBJECT AS B
WHERE B.Artist = A.AName AND B.Id_no in (SELECT B.Id_no
										 FROM ART_OBJECT AS B, SCULPTURE AS S
										 WHERE B.Id_no = S.Id_no)
ORDER BY AName;


/*5) A retrieval query using joined tables*/

SELECT A.Id_no, A.Title, B.Collection
FROM (ART_OBJECT AS A JOIN BORROWED AS B ON A.Id_no = B.Id_no)
WHERE B.Collection = 'Masterpieces of the Louvre';


/*6) An update operation with any necessary triggers*/

/*ALTER TABLE PERMANENT_COLLECTION
	DROP CONSTRAINT FK_UPDATE;*/  /*only needed if executing again*/
ALTER TABLE PERMANENT_COLLECTION
	ADD CONSTRAINT FK_UPDATE
    FOREIGN KEY (Id_no)
    REFERENCES ART_OBJECT (Id_no)
    ON UPDATE CASCADE;

DROP TRIGGER IF EXISTS cost_update;
CREATE TRIGGER cost_update
BEFORE UPDATE ON PERMANENT_COLLECTION
FOR EACH ROW
	SET NEW.Cost= (IF(NEW.Cost >= OLD.Cost,
					NEW.Cost,
                    OLD.Cost));

UPDATE PERMANENT_COLLECTION
SET Cost = Cost * 1.05
WHERE Id_no IN (SELECT Id_no
				 FROM ARTIST AS A, ART_OBJECT AS B
                 WHERE B.Artist = A.AName AND A.AName = 'Benedetto da Rovezzano');


/*7) A deletion operation with any necessary triggers*/

/*ALTER TABLE PERMANENT_COLLECTION
	DROP CONSTRAINT FK_DELETE;*/  /*only needed if executing again*/
ALTER TABLE BORROWED
	ADD CONSTRAINT FK_DELETE
    FOREIGN KEY (Collection)
    REFERENCES COLLECTIONS (CName)
    ON DELETE SET DEFAULT;

SET sql_safe_updates = 0;
DROP TRIGGER IF EXISTS collection_delete;
CREATE TRIGGER collection_delete
AFTER DELETE ON COLLECTIONS
FOR EACH ROW
UPDATE BORROWED
	SET Collection = 'Museum';

DELETE FROM COLLECTIONS
WHERE Type_ = 'Museum';
                 
