import os
from threading import current_thread, Thread
from multiprocessing import current_process
import subprocess
from exception import CustomException
from logger import logging
import sys

def io_bound(image_name):

    logging.info("Entering image scanning function")


    try:    
        with open(f'{image_name}.txt', 'w') as f:
        
            pid = os.getpid()
            threadName = current_thread().name
            processName = current_process().name

            print(f"{pid} * {processName} * {threadName} * {image_name} \
                ---> Start Scanning...")
            
            logging.info("Scanning Docker with trivy")

            scan_image = "trivy -q image -f table {}".format(image_name)
            scan_result = subprocess.check_output(scan_image.split()).decode('utf-8')

            logging.info("creating the report")            
            f.writelines(scan_result)
            
            print(f"{pid} * {processName} * {threadName} * {image_name}  \
                ---> Finished Scanning...")

    except Exception as e:
        CustomException(e,sys)