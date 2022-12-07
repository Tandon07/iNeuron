from flask import Flask,request,jsonify
import mysql.connector as conn
import pymongo

app= Flask(__name__)

# cursor.execute("create database ApiSQLTask")
# cursor.execute("create table ApiSQLTask.apisqltable (Name varchar(25), Id int )" )


@app.route('/insert',methods=['Get','Post'])
def insertdata():
    if(request.method=='POST'):
        name=request.json['name']       #Requesting a json data from the user
        id=request.json['id']
        cursor.execute("Insert into ApiSQLTask.apisqltable (Name, Id)  values (%s,%s)",(name,id))
        mydb.commit()
        return jsonify(str('Succesfully Inserted'))


# 2.  Write a program to update a record via api

@app.route('/update',methods=['Get','Post'])
def updatedata():
    if(request.method=='POST'):
        name=request.json['name']       #Requesting a json data from the user
        cursor.execute("UPDATE ApiSQLTask.apisqltable SET Name = %s WHERE Id = 2",(name,))    # You have to enter name as tuples
        mydb.commit()
        return jsonify(str('Succesfully updated'))


# 3 . Write a program to delete a record via api


@app.route('/delete',methods=['Get','Post'])
def deletedata():
    if(request.method=='POST'):
        id=request.json['id']       #Requesting a json data from the user
        cursor.execute("delete from ApiSQLTask.apisqltable where Id=%s",(id,))    # You have to enter name as tuples
        mydb.commit()
        return jsonify(str('Succesfully delete'))

# 4 . Write a program to fetch a record via api


@app.route('/fetch',methods=['Get','Post'])
def fetchdata():
    if(request.method=='POST'):
        id=request.json['id']       #Requesting a json data from the user
        cursor.execute("select * from ApiSQLTask.apisqltable where Id=%s",(id,))    # You have to enter name as tuples
        for i in cursor.fetchall():
            return jsonify(str(i))
        print("fetched successfully")

# @app.route('/fetch',methods=['Get','Post'])
# def fetchdata():
#     if(request.method=='POST'):
#         id=request.json['id']       #Requesting a json data from the user
#         cursor.execute("select * from ApiSQLTask.apisqltable where Id=%s",(id,))    # You have to enter name as tuples
#         for i in cursor.fetchall():
#             return jsonify(str(i))
#         print("fetched successfully")






if __name__=='__main__':
    app.run()

