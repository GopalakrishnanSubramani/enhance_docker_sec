import time
import multiprocess
from threading import Thread
from multiprocessing import Process
from vars import docker_images
from exception import CustomException
from logger import logging
import sys

class Scanner:
    
    logging.info("Initializing the scanner")

    
    def __init__(self) -> None:
        self.image_name1 = docker_images["image_name1"]
        self.image_name2 = docker_images["image_name2"]
        
    
    def processing(self):
        logging.info("Entering the multithreading fucntion")

        try:
            # self.process = multiprocess.io_bound()
            t1 = Thread(target = multiprocess.io_bound, args =(self.image_name1, ))
            t2 = Thread(target = multiprocess.io_bound, args =(self.image_name2, ))
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        except Exception as e:
            CustomException(e,sys)

if __name__=="__main__":
    start = time.time()

    Scanner().processing()

    end = time.time()
    print('Time taken in seconds -', end - start)