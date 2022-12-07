import logging
logging.basicConfig(filename="Task1Strings.log",level=logging.INFO)

class Task1String:


    logging.info("Welcome to Task1String Assignment")


    


    s = "this is My First Python programming class and i am learNING python string and its function"




# 1 . Try to extract data from index one to index 300 with a jump of 3

    def extract(self,s):
        try:
            logging.info("The entered string is:- %s",s)
            logging.info("Output of the task is:- %s",s[0:300:3])
        except Exception as e :
            logging.info("Exception that we got is %s",e)




# 2. Try to reverse a string without using reverse function

    def reverseString(self,s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s[::-1])
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)




# 3. Try to split a string after conversion of entire string in uppercase

    def splitString(self,s):
        try:
            s=s.upper()
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.split())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)




# 4. try to convert the whole string into lower case

    def lowerCase(self,s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.lower())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)




    # 5 . Try to capitalize the whole string

    def capitalizeString(self,s):

        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.capitalize())
        except Exception as e:
            logging.info("Exception that we got is %s", e)



# 6. Try to give an example of expand tab

    def expandtabString(self,s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s",s.expandtabs())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)

# 7 . Give an example of strip , lstrip and rstrip

    def stripString(self,s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.strip())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)


    def leftStripString(self, s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.lstrip())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)


    def rightStripString(self, s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.strip())
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)



# 8.  Replace a string charecter by another charector by taking your own example "sudhanshu"

    def replaceCharacter(self,s):
        try:
            temp=s
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s",temp.replace("d","e"))
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)



# 9 . Try  to give a defination of string center function with and exmple

    def centerString(self,s):
        try:
            logging.info("The entered string is:- %s", s)
            logging.info("Output of the task is:- %s", s.center(49, "*"))
        except Exception as e:
            logging.info("Exception that we got is:- %s", e)







sudh=Task1String()
sudh.centerString("Center")

