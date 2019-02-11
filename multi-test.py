import multiprocessing
import os
import random
import time

def doit():
    print("I'm proces no %s " % os.getpid())
    print(time.ctime(time.time()))

if __name__=="__main__":
    for n in range(11):
        t = random.randrange(1,5)
        time.sleep(t)
        p=multiprocessing.Process(target = doit)
        p.start()