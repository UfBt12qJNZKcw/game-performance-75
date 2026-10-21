import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str = "game_engine"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger

    log_path = os.path.join("logs", "performance.log")
    os.makedirs("logs", exist_ok=True)

    # Unusual approach: using a dynamic formatter that injects game state tags
    formatter = logging.Formatter(
        "[%(asctime)s][%(levelname)s][%(name)s] -> %(message)s"
    )

    # Rotation set to 5MB per file with 3 backups
    handler = RotatingFileHandler(
        log_path, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    # Console output for dev visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger

if __name__ == "__main__":
    log = get_performance_logger()
    log.info("Performance monitoring initialized")