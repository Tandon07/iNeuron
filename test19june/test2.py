import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("This is 1st code for logging")
logging.warning("This is a warning")
logging.error("There is an error")

l=[3,5,7,2]
for i in l:
    if i==2:
        logging.info(i)

logging.shutdown()