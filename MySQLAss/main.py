import mysql.connector as conn
import pandas as pd

import json

from mysql.connector import cursor


class sqlconn:


    mydb = conn.connect(host = "localhost" , user="root", password="Hellodude123@")

    # print(mydb)
    cursor=mydb.cursor()
    # cursor.execute("create database MySQLAssign")


# QUERY    1. Create a  table attribute dataset and dress dataset


    # s1="create table MySQLAssign.AttributeDataSet5(Dress_ID varchar(25),style varchar(25), Price varchar(25), Rating varchar(25),Size varchar(10),Season varchar(25),NeckLine varchar(25),SleeveLength varchar(25),waiseline varchar(25),Material varchar(25),FabricType varchar(25),Decoration varchar(25),PatternType varchar(25),Recommendation int)"
    #
    # s2="create table MySQLAssign.DressSalesd(Dress_ID int,29_08_2013 int,31_08_2013 int,09_02_2013 int,09_04_2013 int,09_06_2013 int,09_08_2013 int,09_10_2013 int,09_12_2013 int,14_9_2013 int,16_9_2013 int,18_9_2013 int,20_9_2013 int,22_9_2013 int,24_9_2013 int,26_9_2013 int,28_9_2013 int,30_9_2013 int,10_02_2013 int,10_04_2013 int,10_06_2013 int,10_08_2010 int,10_10_2013 int,10_12_2013 int)"
    # cursor.execute(s1)
    # cursor.execute(s2)



# QUERY    2. Do a bulk load for these two table for respective dataset



   # s3="LOAD DATA INFILE 'Attribute DataSet.csv' INTO TABLE MySQLAssign.attributedataset5 FIELDS TERMINATED BY ','LINES TERMINATED BY '\n' IGNORE 1 ROWS;"
   #  cursor.execute(s3)
   #  mydb.commit()
   #  s4="LOAD DATA INFILE 'Dress Salwes.csv' INTO TABLE MySQLAssign.DressSalesd FIELDS TERMINATED BY ','LINES TERMINATED BY '\n' IGNORE 1 ROWS;"
   #  cursor.execute(s4)
   #  mydb.commit()


# Connection to MongoDB is done in different class


# QUERY    6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID

    s6="select * from MySQLAssign.AttributeDataSet5 left join MySQLAssign.DressSalesd ON AttributeDataSet5.Dress_ID=DressSalesd.Dress_ID";

    # cursor.execute(s6)
    # mydb.commit()
    # l = []
    # for i in cursor.fetchall():
    #     l.append(i)
    # print(l)


#  QUERY     7. Write a sql query to find out how many unique dress that we have based on dress id


    s7="SELECT count(DISTINCT(Dress_ID)) FROM MySQLAssign.DressSalesd"
    # cursor.execute(s7)
    # l = []
    # for i in cursor.fetchall():
    #     l.append(i)
    # print(l)


#  QUERY    8. Try to find out how many dress is having recommendation 0


    # s8="select count(*) from MySQLAssign.AttributeDataSet5 where Recommendation=0"
    # cursor.execute(s8)
    # l = []
    # for i in cursor.fetchall():
    #     l.append(i)
    # print(l)


#QUERY    9. Try to find out total dress sell for individual dress id


    s9="select Dress_ID,count(Dress_ID) from MySQLAssign.DressSalesd group by Dress_ID"
    cursor.execute(s9)
    l = []
    for i in cursor.fetchall():
        l.append(i)
    print(l)



# QUERY    10. Try to find out a third highest most selling dress id


    s10=