import pymongo



client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data=[
    {"name": "sudhanshu", "email": "sudh@gmail.com", "surname": ["kumar", "tandon", "suman"]},
    {"name": "sudhanshu", "email": "sudh@gmail.com", "surname": ["kumar", "tandon", "suman"]},
    {"name": "sudhanshu", "email": "sudh@gmail.com", "surname": ["kumar", "tandon", "suman"]}] #IMPORTANT list of dictionaries is called JSON

db1=client['mongotest1']            # mongotest is database name can be anything
coll=db1['test']                   #coll is collection, test is the name of table (in cas of SQL we create table and in case of Mongo we create collection)
coll.insert_many(data)

db2=client['mongotest2']
coll=db2['test3']
coll.insert_many(data)

