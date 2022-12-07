import pymongo



client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
dbase = client.test
print(dbase)

d={
  "markers": [
    {
      "name": "Rixos The Palm Dubai",
      "position": [25.1212, 55.1535],
    },
    {
      "name": "Shangri-La Hotel",
      "location": [25.2084, 55.2719]
    },
    {
      "name": "Grand Hyatt",
      "location": [25.2285, 55.3273]
    }
  ]
}
db1=client['mongotest']            # mongotest is database name can be anything
coll=db1['test']                   #coll is collection, test is the name of table (in cas of SQL we create table and in case of Mongo we create collection)
coll.insert_one(d)

