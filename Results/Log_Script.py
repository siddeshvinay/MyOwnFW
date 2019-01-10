import logging
import os

def writelogs(msg,loglevel):
    try:
        #path=os.path.abspath(__file__+'/../Results/Applogs.txt')
        path='C:/Users/sjanagonnavar/DJFW/Results/Applogs.txt'
        if (loglevel=="warning"):
            logging.basicConfig(filename=path, level=logging.WARNING,
                                format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
            logging.warning(msg)
        elif (loglevel=="Info"):
            logging.basicConfig(filename=path, level=logging.INFO,
                                format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
            logging.info(msg)
        elif loglevel=="Error":
            logging.basicConfig(filename=path, level=logging.ERROR,
                                format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
            logging.error(msg)
        elif loglevel=="Debug":
            logging.basicConfig(filename=path, level=logging.DEBUG,
                                format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
            logging.debug(msg)
        else:
            msg="unble to get the log file"
    except Exception as e:
        msg="Log file is not present"


