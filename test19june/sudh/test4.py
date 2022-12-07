

#   ...................#    R. I. P    Print Statement           #.......................


import logging

logging.basicConfig(filename="test4.log", level=logging.INFO, format='%(asctime)s %(name)s %(message)s %(levelname)s')
def div(a,b):
    logging.info("The num entered by user %s and %s",a,b)

    # %s is a kind of placeholder

    try:
        logging.info("we are into func")
        divi=a/b
        return divi
    except Exception as e:
        logging.exception(e)


print(div(10,0))


#   logging is better than print
