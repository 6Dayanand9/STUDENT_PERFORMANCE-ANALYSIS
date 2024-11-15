import sys
import os
from src.logger import logging
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error Occur in Python Script[{0}] line Number [{1}] and Error message[{2}]'.format(
        filename,
        exc_tb.tb_lineno, 
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
# For Testing Purpose
if (__name__)=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("Dividing By Zero")
        raise CustomException(e,sys)