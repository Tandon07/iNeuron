import logging

logging.basicConfig(filename="test3.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(message)s %(levelname)s')
logging.info("This is my log with timestamp")
