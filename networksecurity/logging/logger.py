import logging 
import os
from datetime import  datetime

#Generating the Log Filename
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Create JUST the folder path (e.g., /current/directory/logs)
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

#Combine folder path and filename
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#Setup logger       
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)                                                                                      