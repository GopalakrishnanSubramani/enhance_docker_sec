import time
import multiprocess
from threading import Thread
from multiprocessing import Process
from get_img import docker_images
from exception import CustomException
from logger import logging
import sys

class Scanner:
    
    logging.info("Initializing the scanner")

    
    def __init__(self) -> None:
        self.image_name1 = docker_images["image_0"]
        self.image_name2 = docker_images["image_1"]
    
    
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
    
    print('******************* Scannig Success ok******************')
    print('Time taken in seconds -', end - start)
