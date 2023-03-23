# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
fmtstr="User: %(user)s | %(asctime)s | [%(levelname)s] %(funcName)s Line %(lineno)d: %(message)s"
datestr="%m/%d/%Y %I:%M:%S %p"
extdata = {"user": "Denny Li"}
def another_function():
    logging.debug("This is a debug level log message", extra=extdata)
# set the output file and debug level, and
# TODO: use a custom formatting specification
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtstr,
                    datefmt=datestr)

logging.info("This is an info-level log message", extra = extdata)
logging.warning("This is a warning-level message", extra=extdata)
another_function()
