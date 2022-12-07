# For MongoDB
from flask import Flask,request,jsonify
import pymongo


app= Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
dbase = client.test
db1 = client['APISQLTask']
coll = db1['test']


@app.route('/mongoinsert',methods=['Get','Post'])
def mongoinsertdata():
    if(request.method=='POST'):
        name=request.json['name']
        id=request.json['id']
        coll.insert_one({name:id})    #IMPORTANT!!!! THE WAY I HAVE WRITTEN {name:id}
        return jsonify(str('Succesfully Inserted'))



if __name__=='__main__':
    app.run(port=5001)
