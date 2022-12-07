import logging
from PIL import Image

# logging.basicConfig(filename="test5.log", level=logging.ERROR, format='%(asctime)s %(name)s %(message)s %(levelname)s')
logging.basicConfig(filename="test6.log", level=logging.CRITICAL, format='%(asctime)s %(name)s %(message)s %(levelname)s')
def div(a,b):
    logging.info("The num entered by user %s and %s",a,b)

    # %s is a kind of placeholder

    try:
        logging.info("we are into func")
        divi=a/b
        return divi
    except Exception as e:
        logging.exception(e)
        print(e)

div(10,0)







# The reason for critical not showing anyting in log is screenshot (13)

