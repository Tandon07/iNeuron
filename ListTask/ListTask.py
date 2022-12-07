import logging
logging.basicConfig(filename="listTask.log",level=logging.DEBUG)

class listTask:


    logging.info("Welcome to List Assignment")

# 1 . Try to reverse a list

    def revList(self,l):
        try:
            l1=l
            logging.info("The entered list is:- %s", l1)
            logging.info("Output of the task is:- %s", l1[::-1])
        except Exception as e:
            logging.info("Exception that we got is %s", e)




# 2. try to access 234 out of this list

    def AccessNo(self,l,n):        #n is the number to access
        try:
            l1 = l
            self.n=n
            logging.info("The entered list is:- %s", l1)

            for i in l1:
                if(i==n):
                    logging.info("%s is available",n)
                    break

        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 3 .  Try to extract only a list collection form list l

    def ExtractList(self,l):
        try:
            l1 = l
            logging.info("The entered list is:- %s", l1)

            for i in l1:
                if(type(i)==list):
                    logging.info("%s",i)

        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 4 . Try to extract "sudh"

    def AccessString(self,l,s):        #s is the string to access
        try:
            l1 = l
            self.s=s
            c=0
            logging.info("The entered list is:- %s", l1)

            for i in l1:
                if(i==s):
                    logging.info("%s is available",s)
                    c+=1
                    break
            if (c == 0):
                logging.info("%s is not available", s)

        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 5 : Try to give summation of all the numeric data

    def sumList(self,l):
        try:
            l1=l
            logging.info("The entered list is:- %s", l1)
            logging.info("Output of the task is:- %s", sum(l1))
        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 6 : Try to filter out all the odd values out all numeric data which is a part of a list

    def extractOdd(self,l):
        try:
            l1 = l
            logging.info("The entered list is:- %s", l1)

            for i in l1:
                if(type(i)==int):
                    if (i % 2 != 0):
                        logging.info("%s", i)

                if(type(i)==list):
                    for j in i:
                        if (type(j) == int):
                            if(j%2!=0):
                                logging.info("%s",j)

        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 7 :Try to find out a number of occurences of all the data

    def countOccurances(self,l):

        try:
            l1 = []
            logging.info("The entered list is:- %s", l)
            for i in l:
                if type(i) == int:
                    l1.append(i)
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l1.append(g)
            for i in set(l1):
               logging.info("%s is %s times",i, l1.count(i))

        except Exception as e:
            logging.info("Exception that we got is %s", e)




# 8: Try to find out multiplication of all numeric value in the individual collection inside dataset


    def multiplyValues(self,l):

        try:
            m=1
            l1 = []
            logging.info("The entered list is:- %s", l)
            for i in l:
                if type(i) == int:
                    l1.append(i)
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            for i in l1:
               m = m * i
            logging.info("multiplication is %s", m)

        except Exception as e:
            logging.info("Exception that we got is %s", e)




# 9: Try to unwrape all the collection inside collection and create a flat list

    def unwrapData(self,l):

        try:
            l1 = []
            logging.info("The entered list is:- %s", l)
            for i in l:
                if type(i) == int or type(i) == str:
                    l1.append(i)
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l1.append(g)
            logging.info("The data in unwrapped format is :- %s",l1)

        except Exception as e:
            logging.info("Exception that we got is %s", e)







# Here I will do creation of object

obj=listTask()
obj.unwrapData([10,2,3,4,5,6,6,6,6,6,7,[11,22,33,44,55,66],111,222,333,234,'umesh',10,4,4,4])