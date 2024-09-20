import logging

def logger_init(name):
    logger = logging.getLogger(name)  # Removed the typo "getLo gger"
    
    # Check if the logger already has handlers to prevent adding multiple handlers
    if not logger.hasHandlers():
        # Configure the logger
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        
        # File handler to save logs to file
        file_handler = logging.FileHandler('all.log')
        file_handler.setFormatter(formatter)
        
        # Stream handler to show logs on the console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        
        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger
