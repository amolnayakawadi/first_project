import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)


log_path_file = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
     filename=log_path_file,
     level=logging.INFO, 
     format= '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -  %(message)s',
)