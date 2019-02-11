import multiprocessing
import os
import random
import time

def theNow(msg):
    time.sleep(random.randrange(1,6))
    print(msg + '\n')
    print("I am process %s \t" % (os.getpid()))
    print("the time is %s" % time.ctime(time.time()))

def do_this(msg):
    theNow(msg)

if __name__ == "__main__":
    for t in range(3):
        print("hello there")
        p = multiprocessing.Process(target = do_this, args = ("I am attempt no %s" % t,))
        p.start
        #theNow()
