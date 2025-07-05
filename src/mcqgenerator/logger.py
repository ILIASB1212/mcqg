import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"


new_dir_path=os.path.join(os.getcwd(),"logs")

os.makedirs(new_dir_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(new_dir_path,LOG_FILE)


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)



