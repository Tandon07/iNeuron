from flask import Flask,request,jsonify
import mysql.connector as conn

app= Flask(__name__)


@app.route('/testfun')
def test():
    get_name=request.args.get("get_name")
    mobile_number=request.args.get("mobile")
    mailID = request.args.get("id")
    # return "This is my first function for GET {}".format(get_name)
    # In the url use /testfun?get_name=saurabh to get output as "This is my first function for GET saurabh"



    return "This is my first function for GET {} {} {}".format(get_name,mobile_number,mailID) #for multiple inputs
# In url use /testfun?get_name=saurabh &mobile=8789499 &id=hjf@gmail.com to get output as "This is my first function for GET saurabh 8789499 hjg@gmail.com"




@app.route('/dbretrive')
def dbase():
    database_name=request.args.get("dn")
    table_name=request.args.get("tn")
    mydb = conn.connect(host="localhost", user="root", password="12345")
    cursor = mydb.cursor()

    cursor.execute(f"select * from {database_name}.{table_name}")
    data=cursor.fetchall()

    return jsonify(data)






if __name__=='__main__':
    app.run(port=5003)

#http://127.0.0.1:5002/dbretrive?dn=apisqltask &tn=ApiSQLTask.apisqltable