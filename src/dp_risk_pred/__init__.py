
import logging
import os,sys
from pathlib import Path
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log" #NAme of log file

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # create logs folder in current working directory
os.makedirs(logs_path,exist_ok=True) # if folder exist then no need to create new folder

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    level= logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]  %(lineno)d - %(levelname)s - %(module)s - %(message)s",

)


logger = logging.getLogger('dp_risk_logger')

