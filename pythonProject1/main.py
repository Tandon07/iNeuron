import pandas as pd
import pymongo



client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db1=client['Mysqlassgn']
coll=db1['solution']