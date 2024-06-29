import logging

# Configure logging settings
logging.basicConfig(
  level = logging.INFO,
  format = '%(asctime)s - %(levelname)s - %(message)s'  # The format will be date time level and actual log content
)

# Logging functions for info and error messages
def log_info(message):
  logging.info(message)

def log_error(message):
  logging.error(message)
