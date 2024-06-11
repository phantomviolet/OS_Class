import threading
import time

#완성

shared_resource = 0
new_lock = threading.Lock()

class SEMAPHORE_CLASS:
    def __init__(self, value):
        self.value = value

S = SEMAPHORE_CLASS(1)

def wait():
    S.value -= 1
    if(S.value < 0):
        new_lock.acquire()
def signal():
    S.value += 1
    if(S.value <= 0):
        new_lock.release()
    
def process_1():
    global shared_resource
    while(True):
        wait()
        try:
            shared_resource = 1
            print("process 1 : %d\n" %shared_resource)
            time.sleep(1)
        finally:
            signal()

def process_2():
    global shared_resource
    while(True) :
        wait()
        try:
            shared_resource = 2
            print("process 2 : %d\n" %shared_resource)
            time.sleep(1)
        finally:
            signal()

thread1 = threading.Thread(target=process_1)
thread2 = threading.Thread(target=process_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
