--Project 2 Team 1
--Matthew McNatt: 1001739201
--Vladimir Caterov: 1002011907
--Harrison Cawood: 1001729180
--Date 4/11/2023

.mode csv
.open Library_Database.db

--SCHECMA SET UP
DROP TABLE IF EXISTS BOOK;
CREATE TABLE BOOK (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT, --Will be assigned automatically on insert
    title VARCHAR(255) NOT NULL, --non unique by choice
    book_author VARCHAR(255) NOT NULL --author cannot be a foreign key because author is name not unique
);

DROP TABLE IF EXISTS BOOK_AUTHORS;
CREATE TABLE BOOK_AUTHORS(
    book_id INT NOT NULL,
    author_name VARCHAR(255) NOT NULL,
    FOREIGN KEY(book_id) REFERENCES BOOK(book_id)
        ON UPDATE CASCADE           ON DELETE CASCADE
);
--Couldnt get the trigger to work in order to update the author table on book insert
--CREATE TRIGGER new_book_insert
--AFTER INSERT ON BOOK
--BEGIN INSERT INTO BOOK_AUTHORS (book_id, author_name)
--VALUES(NEW.book_id, NEW.book_author)
--END;


DROP TABLE IF EXISTS BORROWER;
CREATE TABLE BORROWER (
    card_no INTEGER PRIMARY KEY AUTOINCREMENT, --Will be assigned automatically on insert
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS LIBRARY_BRANCH;
CREATE TABLE LIBRARY_BRANCH (
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_name VARCHAR(255) NOT NULL,
    branch_address VARCHAR(255) NOT NULL
);
DROP TABLE IF EXISTS PUBLISHER;
CREATE TABLE PUBLISHER(
    publisher_name VARCHAR(255) NOT NULL PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS BOOK_COPIES;
CREATE TABLE BOOK_COPIES (
    book_id INTEGER,
    branch_id INT NOT NULL,
    no_of_copies INT DEFAULT 0,
    FOREIGN KEY(book_id) REFERENCES BOOK(book_id)
        ON UPDATE CASCADE           ON DELETE CASCADE,
    FOREIGN KEY(branch_id) REFERENCES LIBRARY_BRANCH(branch_id)
        ON UPDATE CASCADE           ON DELETE CASCADE
);

DROP TABLE IF EXISTS BOOK_LOANS;
CREATE TABLE BOOK_LOANS(
    book_id INT NOT NULL,
    branch_id INT NOT NULL,
    card_no INT NOT NULL,
    date_out VARCHAR(50) NOT NULL,
    due_date VARCHAR(50) NOT NULL,
    returned_date VARCHAR(50),
    FOREIGN KEY(book_id) REFERENCES BOOK(book_id)
        ON UPDATE CASCADE           ON DELETE CASCADE,
    FOREIGN KEY(card_no) REFERENCES BORROWER(card_no)
        ON UPDATE CASCADE           ON DELETE CASCADE,
    FOREIGN KEY(branch_id) REFERENCES LIBRARY_BRANCH(branch_id)
        ON UPDATE CASCADE           ON DELETE CASCADE
);

--import statements
.import Book.csv BOOK
.import Book_Authors.csv BOOK_AUTHORS
.import Publisher.csv PUBLISHER
.import Library_Branch.csv LIBRARY_BRANCH
.import Book_Copies.csv BOOK_COPIES
.import Book_Loans.csv BOOK_LOANS
.import Borrower.csv BORROWER


--Output switch
.mode box --wrap 30
.headers on

SELECT count(*) as Book_Count from BOOK;
SELECT count(*) as Book_Loans_Count from BOOK_LOANS;
SELECT count(*) as Library_Branch_Count from LIBRARY_BRANCH;
SELECT count(*) as Book_Authors_Count from BOOK_AUTHORS;
SELECT count(*) as Book_Copies_Count from BOOK_COPIES;
SELECT count(*) as Borrower_Count from BORROWER;
SELECT count(*) as Publisher_Count from PUBLISHER;

--Queries

--1)
--Insert yourself as a New Borrower. Do not provide the Card_no in your query

INSERT INTO BORROWER (name,address,phone) VALUES('Harrison Cawood', '815 W Abram St, Arlington TX, 76013','(817) 233-2448');

--2)
--Update your phone number to (837) 721-8965

UPDATE BORROWER
SET phone = '(837) 721-8965'
WHERE name = 'Harrison Cawood';


--3)
-- Increase the number of book_copies by 1 for the ‘East Branch’ 
UPDATE BOOK_COPIES
SET no_of_copies = no_of_copies + 1
WHERE BOOK_COPIES.branch_id = (
                            SELECT branch_id
                            FROM LIBRARY_BRANCH
                            WHERE branch_name = 'East Branch');


--4-a)
--Insert a new BOOK with the following info: Title: ‘Harry Potter and the Sorcerer's Stone’ ;
--Book_author: ‘J.K. Rowling’
INSERT INTO BOOK (title, book_author)
VALUES ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling');

--4-b)
--You also need to insert the following branches:
--North Branch 456 NW, Irving, TX 76100
--UTA Branch 123 Cooper St, Arlington TX 76101

INSERT INTO LIBRARY_BRANCH (branch_name, branch_address)
VALUES ('North Branch', '456 NW, Irving, TX 76100'),
       ('UTA Branch', '123 Cooper St, Arlington TX 76101');


--5)
--Return all Books that were loaned between March 5, 2022 until March 23, 2022. List Book
--title and Branch name, and how many days it was borrowed for.
SELECT B.title, LB.branch_name, julianday(BL.returned_date)-julianday(BL.date_out) AS Daysborrowed
FROM BOOK as B
JOIN BOOK_LOANS as BL ON BL.book_id = B.book_id
JOIN LIBRARY_BRANCH as LB ON LB.branch_id = BL.branch_id
WHERE BL.date_out >= '2022-03-05' AND BL.returned_date <= '2022-03-23';


--6)
--Return a List borrower names, that have books not returned

SELECT name
FROM BORROWER as B
WHERE B.card_no = (SELECT card_no
                   FROM BOOK_LOANS
                   WHERE returned_date <> NULL);


--7)
-- Create a report that will return all branches with the number of books borrowed per branch
--separated by if they have been returned, still borrowed, or late. 


--8)
--What is the maximum number of days a book has been borrowed
SELECT BOOK.title, MAX(julianday(BL.returned_date)-julianday(BL.date_out)) as MaxDaysBorrowed
FROM BOOK
JOIN BOOK_LOANS as BL ON BL.book_id = BOOK.book_id
GROUP BY BOOK.book_id
;


--9)
--Create a report for Ethan Martinez with all the books they borrowed. List the book title and
--author. Also, calculate the number of days each book was borrowed for and if any book is late in return
--date. Order the results by the date_out


--10)
--Return all borrowers and their addresses that borrowed a book
SELECT name, address
FROM BORROWER as B
JOIN BOOK_LOANS on B.card_no = BOOK_LOANS.card_no;


