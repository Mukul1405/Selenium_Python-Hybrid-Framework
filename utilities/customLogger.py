import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log", level=logging.INFO, filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        if not logger.propagate:
            print("Logger propagation is set to False")
        else:
            print("Logger propagation is set to True")

        logger.propagate = True
        return logger
