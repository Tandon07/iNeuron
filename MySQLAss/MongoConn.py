import pymongo
import pandas as pd
from main import sqlconn

import json
from pymongo import MongoClient


class mongoconn(sqlconn):
    client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    print(db)
    db1=client['Mysqlassgn']
    coll=db1['solution']



# QUERY    3. read these dataset in pandas as a dataframe



    df = pd.read_csv("C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Attribute DataSet.csv")
    df2 = pd.read_csv("C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Dress Sales.csv")
    print(type(df2))



#QUERY    4. Convert attribute dataset in json format



    df.to_json("C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Attribute DataSet.json")



#QUERY    5. Store this dataset into mongodb


    #        One Method which didn't work

    # dfToJson = pd.read_json("C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Attribute DataSet.json")
    # dff = list(dfToJson)
    # print(type(dff))
    # print(dfToJson)

    #        The Method which worked


    with open('C:\ProgramData\MySQL\MySQL Server 8.0\Data\mysqlassign\Attribute DataSet.json') as file:
        file_data = json.load(file)
    coll.insert_one(file_data)


