from src.MLPROJECT.logger import logging
from  src.MLPROJECT.exception import CustomException 
import sys


if __name__=='__main__':
    logging.info("the execution has started")



    try:
        a=1/0

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

    
