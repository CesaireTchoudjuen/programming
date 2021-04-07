# Demonstrate logging
# Attributes you can put in the basicConfig
    # level
    # filename
    # filemode
    # format
        # %(name)s - %(nlevelame)s - %(message)s - %(asctime)s - %(lineno)s 
# By default it will print out from warning andd higher
# If we want to change this: logging.basicConfig(level=logging.INFO)
# logging.basicConfig(filename= 'debugging.log', filemodee='a', level=logging.DEBUGO) will print the debug logs in a file

import logging

name = 'Joe'

logging.basicConfig(
    filename= './debugging.log', 
    filemode='a', level=logging.DEBUG, 
    format='%(name)s - %(nlevelame)s - %(message)s - %(asctime)s - line: %(lineno)s')

logging.error("This is an error")
logging.critical("This is a critical level message")
logging.warning('Dont know %s', name)
logging.info("Still going")
logging.debug("And so is this!")