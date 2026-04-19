from us_visa.logger import logging
# logging.info("This is a info message")

from us_visa.exception import UsVisaException
import sys

try:
    a=2/0

except Exception as e:
    raise UsVisaException(e,sys)    