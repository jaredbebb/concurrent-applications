"""
Built on python 3.7.6
"""

import threading
import logging
import time


"""
define logger
"""
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def hi(name="world"):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    print(f"hello {name}")
    logging.info("Thread %s: finishing", name)


"""
Define thread1
"""
thread1 = threading.Thread(target=hi, args=(f"{__file__}",))
thread1.start()

logging.info("Main    : wait for the thread to finish")
logging.info(f"alive: {thread1.is_alive()}")

print("done")