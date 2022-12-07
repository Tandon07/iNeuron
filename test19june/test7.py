import logging

# logging.basicConfig(filename="test7.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(message)s %(levelname)s')
# logging.basicConfig(filename="test7.log", level=logging.CRITICAL, format='%(asctime)s %(name)s %(message)s %(levelname)s')
logging.basicConfig(filename="test7.log", level=logging.INFO, format='%(asctime)s %(name)s %(message)s %(levelname)s')
try:
    logging.info("I am trying to read a file")
    with open("sudh.txt","r"):
        logging.info("Successfully it has read the file")

except Exception as e:
    logging.critical("This is a critical situation for us")
    logging.error(e)
    logging.exception(e)