from dotenv import dotenv_values
import logging

# Get the environment variables
env_variables = dotenv_values()

# Define a logger
logger = logging.getLogger("logger")
logger.setLevel(env_variables['LOG_LEVEL'])

# Get Stream Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(env_variables['LOG_LEVEL'])

# Formatter
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(module)s - %(funcName)s | %(message)s')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

