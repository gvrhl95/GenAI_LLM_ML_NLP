#Logging is to track any execution that should be able to log all the information into the text file including errors and all
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create the "logs" directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set to DEBUG to capture all messages
)