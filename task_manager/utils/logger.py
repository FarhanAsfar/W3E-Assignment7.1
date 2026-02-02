import logging from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=5*1024*1024, 
        backupCount=5
    )

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger