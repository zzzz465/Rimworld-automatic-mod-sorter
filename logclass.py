import logging
import time
import logging

class Log(logging.Logger):
    def __init__(self):
        self.format1 = str(time.strftime('%j - %H:%M:%S'))
        self.formatter = logging.Formatter(self.format1, ' [%(levelname)s] : %(message)s')

        self.logger = logging.getLogger("RAMS")
        self.logger.setLevel(logging.INFO)
        
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)

        self.file_handler = logging.StreamHandler()
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        self.logger.propagate = 0
        
        