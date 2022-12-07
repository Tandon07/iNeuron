import pymongo



client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
dbase = client.test
print(dbase)


db1=client['mongotest1']            # mongotest is database name can be anything
coll=db1['test11']                   #coll is collection, test is the name of table (in cas of SQL we create table and in case of Mongo we create collection)
# coll.insert_one(d)



        # EXTRACTING data from databse is the most important thing



# record=coll.find()
# for i in record:
#   print(i)



# just to filter out the data of 'position'


# record1 = coll.find({"name": "Rixos The Palm Dubai"})
#
# for i in record1:
#   print(i)



# To extract data whose name starts with greater than "H"


record1 = coll.find({"name": {"$gt":"H"}})
for i in record1:
  print(i)








import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collect = database["table"]
collect.insert_many(data)
# dd=collect.find({"status":"A"})
# for i in dd:
#   print(i)


# dd=collect.find({"status": {'$in':['A','P']}})        #Either A or P
# for i in dd:
#   print(i)
#

#
# dd=collect.find({"status": {'$gt':"C"}})        #Greater than C
# for i in dd:
#   print(i)
#


# dd = collect.find({"qty": {'$gte': 100}})          # Greater than or equal to 100


# dd = collect.find({"item": "sketch pad",'qty':95})

# dd = collect.find({"item": "sketch pad",'qty':{"$gte":75}})


# dd = collect.find({'$or':[{"item": "sketch pad",'qty':{"$gte":75}}]})



# collect.update_one({'item': 'sketch pad'}, {"$set":{'item': 'no. 1'}})
# dd=collect.find({'item': 'no. 1'})


# collect.delete_one({'item': 'no. 1'})             #delete karega ek record ko bas. jitna baar query excecute karenge utna baar ekek kar ke delete karega
dd=collect.find({'item': "sketch pad",'qty':95})


for i in dd:
  print(i)






