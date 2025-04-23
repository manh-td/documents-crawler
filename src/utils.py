import logging
import os
from .config import (
    PRODUCT,
    LOGS_DIR,
)

log_file_path = os.path.join(LOGS_DIR, 'logs.log')
logging.basicConfig(
    force=True,
    level=logging.INFO if PRODUCT else logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
    ] if PRODUCT else [
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)