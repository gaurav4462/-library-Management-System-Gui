import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="gaurav"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE lms")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="gaurav",
  database="lms"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE INFO (
                    Name1 VARCHAR(25),
                    User_Name VARCHAR(25) primary key,
                    EMAIL VARCHAR(50),
                    GENDER char(10),
                    CONTACT VARCHAR(15),
                    password_ VARCHAR(20));""")
mycursor.commit()

mycursor = mydb.cursor()

mycursor.execute("""Create table book_details
                    (BOOK_CODE Varchar(10) primary key, 
                    BOOK_TITLE Varchar(50) NOT NULL,
                    CATEGORY Varchar(15) NOT NULL,
                    AUTHOR Varchar(30) NOT NULL,
                    PUBLICATION Varchar(30),
                    PUBLISH_DATE Date,
                    BOOK_EDITION int(2),
                    PRICE decimal(8,2) NOT NULL, 
                    RACK_NUM Varchar(3),
                    DATE_ARRIVAL Date NOT NULL,  
                    SUPPLIER_ID Varchar(3) NOT NULL
                    );""")
mycursor.commit()


mycursor = mydb.cursor()

mycursor.execute("""Create table av_book
                    (BOOK_CODE Varchar(10) primary key, 
                    BOOK_TITLE Varchar(50) NOT NULL,
                    CATEGORY Varchar(15) NOT NULL,
                    AUTHOR Varchar(30) NOT NULL,
                    PUBLICATION Varchar(30),
                    PUBLISH_DATE Date,
                    BOOK_EDITION int(2),
                    PRICE decimal(8,2) NOT NULL, 
                    RACK_NUM Varchar(3),
                    DATE_ARRIVAL Date NOT NULL,  
                    SUPPLIER_ID Varchar(3) NOT NULL
                    );""")
mycursor.commit()

mycursor = mydb.cursor()

mycursor.execute("""Create table BOOK_ISSUE
                    (User_Name Varchar(20) NOT NULL,
                    BOOK_CODE Varchar(10) NOT NULL,
                    DATE_ISSUE Date NOT NULL,
                    DATE_RETURN Date NOT NULL
                    );""")
mycursor.commit()

mycursor = mydb.cursor()

query="""INSERT INTO BOOK_DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
val = ('BL000011', 'Java ForvDummies', 'JAVA', 'Paul J. Deitel', 'Prentice Hall', '1999-12-10', 9, 600.00, 'A1', '2011-05-10', 'S01')

mycursor.execute(query, val)

mydb.commit()

mycursor = mydb.cursor()

query="""INSERT INTO BOOK_DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
val = ('BL000012', 'Java: The Complete Reference ', 'JAVA', 'Herbert Schildt', 'Tata Mcgraw Hill ', '2011-10-10', 5, 750.00, 'A1', '2011-05-10', 'S03')

mycursor.execute(query, val)

mydb.commit()


mycursor = mydb.cursor()

query="""INSERT INTO av_book VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
val = ('BL000011', 'Java ForvDummies', 'JAVA', 'Paul J. Deitel', 'Prentice Hall', '1999-12-10', 9, 600.00, 'A1', '2011-05-10', 'S01')

mycursor.execute(query, val)

mydb.commit()

mycursor = mydb.cursor()

query="""INSERT INTO av_book VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
val = ('BL000012', 'Java: The Complete Reference ', 'JAVA', 'Herbert Schildt', 'Tata Mcgraw Hill ', '2011-10-10', 5, 750.00, 'A1', '2011-05-10', 'S03')

mycursor.execute(query, val)

mydb.commit()