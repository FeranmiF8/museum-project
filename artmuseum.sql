DROP DATABASE IF EXISTS ARTMUSEUM;
CREATE DATABASE ARTMUSEUM; 
USE ARTMUSEUM;

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST
( AName                  VARCHAR(30)         NOT NULL,
  DateBorn               DATE,
  Date_died              DATE,
  Country_of_origin      VARCHAR(20),
  Epoch                  VARCHAR(25),
  Main_style             VARCHAR(25),
  Description_           VARCHAR(150),
CONSTRAINT ARTISTPK	PRIMARY KEY (AName)
);

INSERT INTO ARTIST
VALUES      ('Benedetto da Rovezzano', '1474-03-08', '1552-09-07', 'Italy', 'Renaissance', 'Sculpting', 'Italian architect and sculptor who worked mainly in Florence during the Renaissance.'),
            ('Guillim Scrots', '1537-08-23', '1553-09-10', 'Belgium', 'Renaissance', 'Mannerist', 'Painter of the Tudor  court and an exponent of the Mannerist style of painting in the Netherlands.'),
            ('Hans Eworth', '1520-06-15', '1574-09-20', 'Belgium', 'Renaissance', 'Allegory', 'Flemish painter who was known for painting allegorical mages as well as portraits of the genetry and nobility.'),
            ('Simone Leigh', '1967-02-24', null, 'United States', 'Modern', 'Expressionism', 'American artist known for working in African art and vernacular objects.'), 
            ('Michelangelo', '1475-03-06', '1564-02-18', 'Italy', 'Renaissance', 'Mannerist', 'Italian sculptor, painter, architect, and poet of the High Renaissance.'),
            ('Jacob Blanck', '1650-05-09', '1690-03-01', 'France', 'Renaissance', 'Mannerist', 'French artist of the High Renaissance.'),
            ('Jean Louis Couasnon', '1747-10-10', '1812-12-15', 'France', 'Renaissance', 'Sculpting', 'French scultor who specialized in portraits of living people.'),
            ('Leonardo da Vinci', '1452-04-15', '1519-05-02', 'Italy', 'Renaissance', 'Realism', 'Italian painter, scientist, theorist, sculptor, and architect known for epitomizing the Renaissance humanist ideal.'),
            ('David D\'Angers', '1788-03-12', '1856-01-04', 'France', 'Renaissance', 'Romanticism', 'French sculptor, medalist, and active freemason.'),
            ('Unknown', null, null, null, null, null, null);

DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS
( EName                  VARCHAR(40)         NOT NULL,
  Start_date             DATE,
  End_date               DATE,
PRIMARY KEY (EName)
);

INSERT INTO EXHIBITIONS
VALUES      ('Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
            ('Modern Gallery', '2022-06-06', '2022-10-20'),
            ('National Estate of Versailles', '2009-10-19', '2010-02-07'),
            ('National Museum of Art', '2009-06-23', '2009-09-24');

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT
( Id_no           CHAR(9)         NOT NULL,
  Year_           INT,
  Title           VARCHAR(50)     NOT NULL      DEFAULT "Untitled",
  Origin          VARCHAR(25),
  Epoch           VARCHAR(25),
  Artist          VARCHAR(25)     NOT NULL      DEFAULT "Unknown",
  Exhibition      VARCHAR(55),
PRIMARY KEY (Id_no),
FOREIGN KEY (Artist) REFERENCES ARTIST(AName),
FOREIGN KEY (Exhibition) REFERENCES EXHIBITIONS(EName)
);

INSERT INTO ART_OBJECT
VALUES      ('123456789', 1500, 'Candelabrum', 'Italian', 'Renaissance', 'Benedetto da Rovezzano', 'Art and Majesty in Renaissance England'),
            ('987654321', 1524, 'Angel Bearing Candlestick', 'Italian', 'Renaissance', 'Benedetto da Rovezzano', 'Art and Majesty in Renaissance England'),
            ('111222333', 1547, 'Edward VI', 'Flemish', 'Renaissance', 'Guillim Scrots', 'Art and Majesty in Renaissance England'),
            ('191919191', 1554, 'Mary I', 'Flemish', 'Renaissance', 'Hans Eworth', 'Art and Majesty in Renaissance England'),
            ('777777777', 1520, 'Furnishing Textile', null, 'Renaissance', 'Unknown', null),
            ('202020202', 2019, '108 (Face Jug Series)', 'American', 'Modern', 'Simone Leigh', 'Modern Gallery'),
            ('196907030', 1562, 'The Wedding at Cana', 'Italian', 'Renaissance', 'Paolo Caliari', null),
            ('201039500', 1513, 'Rebel Slave', 'Italian', 'Renaissance', 'Michelangelo', null),
            ('900234560', 1675, 'Chest of Jewels of Louis XIV', 'French', 'Renaissance', 'Jacob Blanck', 'National Estate of Versailles'),
            ('569123210', 1784, 'Alexandrine Émilie Brongniart', 'French', 'Renaissance', 'Jean Louis Couasnon', 'National Museum of Art'),
            ('379212540', 1503, 'Monna Lisa', 'Italian', 'Renaissance', 'Leonardo da Vinci', 'National Museum of Art'),
            ('621350941', 1802, 'Victor-Hugo', 'French', 'Renaissance', 'David D\'Angers', null);

DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION
( Id_no                  CHAR(9)           NOT NULL,
  Date_acquired          DATE,
  Status_                VARCHAR(15),
  Cost                   DECIMAL(10,2),
PRIMARY KEY (Id_no),
FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

INSERT INTO PERMANENT_COLLECTION
VALUES      ('123456789', '1931-09-04', 'on display', 150000.00),
            ('987654321', '1931-03-07', 'on display', 160000.00),
            ('111222333', '1947-10-06', 'on display', 100000.00),
            ('191919191', '1935-01-04', 'on display', 80000.00),
            ('777777777', '1966-08-09', 'stored', 50000.00),
            ('202020202', '2019-02-07', 'on display', 5000.00);


DROP TABLE IF EXISTS COLLECTIONS;
CREATE TABLE COLLECTIONS
( CName                  VARCHAR(40)           NOT NULL,
  Type_                  VARCHAR(15),
  Description_           VARCHAR(200),
  Address                VARCHAR(50),
  Phone                  VARCHAR(12),
  Contact_person         VARCHAR(20),
PRIMARY KEY (CName)
);

INSERT INTO COLLECTIONS
VALUES      ('Masterpieces of the Louvre', 'Museum', 'Masterpieces bear witness to the wealth of the Louvre\'s collections and the wide range of artistic practices.', '99 rue de Rivoli, 75001 Paris, France', 33140205317, null),
            ('The Art of Portraiture', 'Museum', 'Explore portraiture through the ages with sculptures, paintings, drawings and engravings of emblematic figures.', '99 rue de Rivoli, 75001 Paris, France', 33140205317, null);


DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED
( Id_no                  CHAR(9)           NOT NULL,
  Date_Borrowed          DATE,
  Date_returned          DATE,
  Collection             VARCHAR(50),
PRIMARY KEY (Id_no),
FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no),
FOREIGN KEY (Collection) REFERENCES COLLECTIONS(CName)
);

INSERT INTO BORROWED
VALUES      ('196907030', '1978-01-02', null, 'Masterpieces of the Louvre'),
            ('201039500', '1985-08-03', null, 'Masterpieces of the Louvre'),
            ('900234560', '1990-06-03', null, 'Masterpieces of the Louvre'),
            ('569123210', '1992-03-10', null, 'The Art of Portraiture'),
            ('379212540', '1983-06-02', null, 'The Art of Portraiture'),
            ('621350941', '1990-05-04', null, 'The Art of Portraiture');


DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING
( Id_no                  CHAR(9)           NOT NULL,
  Paint_type             VARCHAR(20),
  Drawn_on               VARCHAR(20),
  Style                  VARCHAR(20),
PRIMARY KEY (Id_no),
FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

INSERT INTO PAINTING
VALUES      ('111222333', 'Oil', 'Wood', 'Mannerist'),
            ('191919191', 'Oil', 'Wood', 'Allegory'),
            ('196907030', 'Oil', 'Canvas', 'Mannerist'),
            ('379212540', 'Oil', 'Wood', 'Sfumato');


DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE
( Id_no                  CHAR(9)           NOT NULL,
  Material               VARCHAR(20),
  Height                 DECIMAL,    /* in cm */
  Weight                 DECIMAL,    /* in kg */
  Style                  VARCHAR(20),
PRIMARY KEY (Id_no),
FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

INSERT INTO SCULPTURE
VALUES      ('123456789', 'Bronze', 340, 622, 'Rococo'),
            ('987654321', 'Bronze', 101, 141, 'Rococo'),
            ('201039500', 'Marble', 215, 916, 'Baroque'),
            ('569123210', 'Marble', 44.2, 600, 'Baroque');

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER
( Id_no                  CHAR(9)           NOT NULL,
  Type_                  VARCHAR(20),
  Style                  VARCHAR(20),
PRIMARY KEY (Id_no),
FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

INSERT INTO OTHER
VALUES      ('777777777', 'Textile', 'Velvet textile'),
            ('202020202', 'Pottery', 'Salt-fired Porcelain'),
            ('900234560', 'Box', 'Gold and oak chest'),
            ('621350941', 'Medallion', 'Plaster');
