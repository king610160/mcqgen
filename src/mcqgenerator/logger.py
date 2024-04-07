import logging
import os
from datetime import datetime

# this is generate log file
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# this is log file's path
log_path=os.path.join(os.getcwd(),"logs")

# if not file, then create the folder, else neglect it
os.makedirs(log_path,exist_ok=True)

# logfile's path
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

# use basicConfig to record logging
logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        # asc is current time, line number, name, level and message
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)