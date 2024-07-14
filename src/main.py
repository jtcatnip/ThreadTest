import logging
import threading
import time
import thread1
import thread2
from src.thread1 import Thread1


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    formatting = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatting, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")

    t2 = thread2.Thread2("new one")
    t2.wait(3)
    t1: Thread1 = thread1.Thread1("cat")
    print("sum:", t1.add(3, 4))
    print("sub:", t1.sub(3, 4))
    print("static test: ", thread2.Thread2.get_value(55))

