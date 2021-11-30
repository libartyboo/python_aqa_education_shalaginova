-- This is an SQLite tutorial / cheat sheet by Kurt Schwehr, 2009

-- Conventions:
--   All SQL keyworks are written UPPERCASE, other stuff lowercase
--   All SQLite commands start with a "."

-- Two dashes start a comment in SQL
/* Another style of comments */

----------------------------------------
-- Setup SQLite for the tutorial
----------------------------------------

-- Ask SQLite for instructions
.help

-- Repeat every command for this tutorial
.echo ON

-- Ask SQLite to print column names
.header ON

-- Switch the column separator from '|' to tabs
.separator "\t"

-- Make SQLite print "Null" rather than blanks for an empty field
.nullvalue "Null"

-- Dump the settings before we go on
.show

----------------------------------------
-- Additional resources
----------------------------------------

-- This tutorial misses many important database concepts (e.g. JOIN and SUBQUERIES)

-- http://swc.scipy.org/lec/db.html

----------------------------------------
-- Basics
----------------------------------------

-- All SQL command end with a semicolon
-- Commands to query the database engine start with SELECT.

-- First hello world:
SELECT "hello world";

-- What is the current date and time?
SELECT CURRENT_TIMESTAMP;

-- Simple math
SELECT 1+2;

-- Calling a function
SELECT ROUND(9.8);

-- Multiple columns are separated by ","
SELECT "col1", "col2";

-- Label columns with AS
SELECT 1 AS first, 2 AS second;

----------------------------------------
-- Time to make a database table!
----------------------------------------

-- Create a first table containing two numbers per row
-- The table name follewd by pairs of <variable name>, <type> in ()
CREATE TABLE tbl_one (a INTEGER, b INTEGER, c INTEGER);

-- List all tables
.tables

-- List the CREATE commands for all tables
.schema

-- Add some data to the table
INSERT INTO tbl_one (a,b,c) VALUES (1,2,3);
INSERT INTO tbl_one (a,b,c) VALUES (4,5,6);
INSERT INTO tbl_one (a,b,c) VALUES (4,17,19);
INSERT INTO tbl_one (a,b,c) VALUES (42,8,72);

-- Show all of the data in the tables
SELECT * FROM tbl_one;

-- Show a smaller number of rows from the table
SELECT * FROM tbl_one LIMIT 2;

-- Only show a subset of the rows
SELECT a,c FROM tbl_one;

-- Fetch only rows that meet one criteria
SELECT * FROM tbl_one WHERE a=4;

-- Fetch only rows that meet multiple criteria
SELECT * FROM tbl_one WHERE a=4 AND b=5;

-- Fetch only rows that meet one of multiple criteria
SELECT * FROM tbl_one WHERE a=1 OR b=47;

-- Greater and less than comparisons work too
SELECT * FROM tbl_one WHERE b >= 8;

-- List all that are not equal too
SELECT * FROM tbl_one WHERE a <> 4;

-- Or list from a set of items
SELECT c,b FROM tbl_one WHERE c IN (3, 19, 72);

-- Order the output base on a field / column
SELECT * FROM tbl_one ORDER BY b;

-- Flip the sense of the order
SELECT * FROM tbl_one ORDER BY b DESC;

-- How many rows in the table?
SELECT COUNT(*) FROM tbl_one;

-- List the unique values for column a
SELECT DISTINCT(a) FROM tbl_one;

-- Count the distinct values for column a
SELECT COUNT(DISTINCT(a)) FROM tbl_one;

-- Get the minumum, maximum, average, and total values for column a
SELECT MIN(a),MAX(a), AVG(a), TOTAL(a) FROM tbl_one;

-- Remove a rows from the table
DELETE FROM tbl_one WHERE a=4;

-- See that we have gotten rid of two rows
SELECT * FROM tbl_one;

-- Adding more data.  You can leave out the column/field names
INSERT INTO tbl_one VALUES (101,102,103);

-- Delete a table
DROP TABLE tbl_one;

----------------------------------------
-- Time to try more SQL data types

-- There are many more types.  For example, see:
-- http://www.postgresql.org/docs/current/interactive/datatype.html

-- WARNING: SQLite plays fast and loose with data types
-- We will pretend this is not so for the next section

-- Make a table with all the different types in it
-- We will step through the types
CREATE TABLE tbl_two (
       an_int   INTEGER,
       a_key    INTEGER PRIMARY KEY,
       a_char   CHAR,
       a_name   VARCHAR(25),
       a_text   TEXT,
       a_dec    DECIMAL(4,1),
       a_real   REAL,
       a_bool   BOOLEAN,
       a_bit    BIT,
       a_stamp  TIMESTAMP,
       a_xml    XML
       );

-- If we add a row that is just an integer, all the fields
-- except a_key will be empty (called 'Null').
-- If you don't specify the primary key value, it will be
-- created for you.
INSERT INTO tbl_two (a_name) VALUES (42);

-- See what you just added.  There will be a number of 'Null' columns
SELECT * FROM tbl_two;

-- A single character
INSERT INTO tbl_two (a_char) VALUES ('z');

-- VARCHAR are length limited strings.
-- The number in () is the maximum number of characters
INSERT INTO tbl_two (a_name) VALUES ('up to 25 characters');

-- TEXT can be any amount of characters
INSERT INTO tbl_two (a_text) VALUES ('yada yada...');

-- DECIMAL specifies an number with a certain number of decimal digits
INSERT INTO tbl_two (a_dec) VALUES

-- Booleans can be true or false
INSERT INTO tbl_two (a_bool) VALUES ('TRUE');
INSERT INTO tbl_two (a_bool) VALUES ('FALSE');

-- Adding bits
INSERT INTO tbl_two (a_bit) VALUES (0);
INSERT INTO tbl_two (a_bit) VALUES (1);

-- Adding timestamps... right now
INSERT INTO tbl_two (a_stamp) VALUES (CURRENT_TIMESTAMP);

-- Date, time, or both.  Date is year-month-day.
INSERT INTO tbl_two (a_stamp) VALUES ('2009-03-15');
INSERT INTO tbl_two (a_stamp) VALUES ('9:02:15');
INSERT INTO tbl_two (a_stamp) VALUES ('2009-03-15 9:02:15');

-- Using other timestamps
INSERT INTO tbl_two (a_stamp) VALUES (datetime(1092941466, 'unixepoch'));
INSERT INTO tbl_two (a_stamp) VALUES (strftime('%Y-%m-%d %H:%M', '2009-03-15 14:02'));

-- XML markup
INSERT INTO tbl_two (a_xml) VALUES ('<start>Text<tag2>text2</tag2></start>');

-- Now you can search by columns being set (aka not Null)
SELECT a_key,a_stamp from tbl_two WHERE a_stamp NOT NULL;

----------------------------------------
-- Putting constraints on the database
-- and linking tables

-- NOT NULL forces a column to always have a value.
--   Inserting without a value causes an error
-- UNIQUE enforces that you can not make entries that are the same
-- DEFAULT sets the value if you don't give one
-- REFERENCES adds a foreign key pointing to another table
CREATE TABLE tbl_three (
       a_key     INTEGER PRIMARY KEY,
       a_val     REAL    NOT NULL,
       a_code    INTEGER UNIQUE,
       a_str     TEXT    DEFAULT 'I donno',
       tbl_two   INTEGER,
       FOREIGN KEY(tbl_two) REFERENCES tbl_two(a_key, an_int)
       );

-- a_key and a_str are automatically given values
INSERT INTO tbl_three (a_val,a_code,tbl_two) VALUES (11.2,2,1);
INSERT INTO tbl_three (a_val,a_code,tbl_two) VALUES (12.9,4,3);

-- This would be an SQL error, as the table already has a code of 2
-- INSERT INTO tbl_three (a_code) VALUES (2);

-- This would be an SQL error, as it has no a_val (which is NOT NULL)
--INSERT INTO tbl_three (a_code) VALUES (3);

SELECT * FROM tbl_three;

-- We can now combine the two tables.  This is called a 'join'
-- It is not required to have foreign keys for joins
SELECT tbl_three.a_code,tbl_two.* FROM tbl_two,tbl_three WHERE tbl_two.a_key == tbl_three.tbl_two;

----------------------------------------
-- Extras for speed

-- For more on speed, see:
-- http://web.utk.edu/~jplyon/sqlite/SQLite_optimization_FAQ.html

-- TRANSACTIONs let you group commands together.  They all work or if there is
-- trouble, they all fail.  Transactions are faster than one at a time too!
-- You can also write "COMMIT;" to end a transaction
BEGIN TRANSACTION;
CREATE TABLE tbl_four (
       a_key    INTEGER PRIMARY KEY,
       sensor   REAL,
       log_time TIMESTAMP);
INSERT INTO tbl_four VALUES (0,3.14,'2009-03-15 14:02');
INSERT INTO tbl_four VALUES (1,3.00,'2009-03-15 14:03');
INSERT INTO tbl_four VALUES (2,2.74,'2009-03-15 14:04');
INSERT INTO tbl_four VALUES (3,2.87,'2009-03-15 14:05');
INSERT INTO tbl_four VALUES (4,3.04,'2009-03-15 14:06');
END TRANSACTION;
ROLLBACK;

-- INDEXes are important if you are searching on a particular field
-- or column often.  It might take a while to create the index,
-- but once it is there, searching on that column is faster
CREATE INDEX log_time_indx ON tbl_four(log_time);

-- INDEXes are automatically created for PRIMARY KEYs and UNIQUE fields

-- Run vacuum if you have done a lot of deleting of tables or rows
VACUUM;

----------------------------------------
-- Find out SQLite's internal state
----------------------------------------
SELECT * FROM sqlite_master;