
"""
 This app will run in the background as a daemon
 """

import threading
import logging
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


x = threading.Thread(target=thread_function, args=(1,), daemon=True)
print("done")