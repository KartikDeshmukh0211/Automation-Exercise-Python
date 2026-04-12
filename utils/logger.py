import logging
import os
from datetime import datetime


def get_logger(name: str):
    logger = logging.getLogger(name)
    print("LOGGER FUNCTION CALLED")

    if logger.handlers:
        return logger

    print("LOGGER FUNCTION CALLEDdf")

    logger.setLevel(logging.INFO)

    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_{timestamp}.log")

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # for printing logs in console
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    # console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger