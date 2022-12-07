# Debug-10
# info 20
# warning-30
# error-40
# critical-50


import logging

# logging.basicConfig(filename="test5.log", level=logging.ERROR, format='%(asctime)s %(name)s %(message)s %(levelname)s')
logging.basicConfig(filename="test5.log", level=logging.DEBUG, format='%(asctime)s %(name)s %(message)s %(levelname)s')
def div(a,b):
    logging.info("The num entered by user %s and %s",a,b)

    # %s is a kind of placeholder

    try:
        logging.info("we are into func")
        divi=a/b
        return divi
    except Exception as e:
        logging.exception(e)

div(10,5)
