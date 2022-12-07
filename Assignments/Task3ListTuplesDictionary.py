import logging
logging.basicConfig(filename="TupDictSetTask.log",level=logging.DEBUG)

class TupDictSetTask:


logging.info("Welcome to TupDictSetTask Assignment")


# 1: Try to list all the key in dict element available in list
    def dictKey(self,l):
        l1=[]
        try:
            for i in l:
                if type(i)==dict:
                    for j in i:
                        logging.info(i.keys())

        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 2: Try to extract all the value element form dict available in list
    def dictValues(self,l):
        l1=[]
        try:
            for i in l:
                if type(i)==dict:
                    for j in i:
                        logging.info(i.values())

        except Exception as e:
            logging.info("Exception that we got is %s", e)

# 3 : Try to find out number of keys in dict element


    def noOfKeys(self,l):
        try:
            for i in l:
                if type(i) == dict:
                    logging.info(len(i))

        except Exception as e:
            logging.info("Exception that we got is %s", e)













obj=TupDictSetTask()
obj.noOfKeys([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])


