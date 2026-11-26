import threading
import time

def greet():
    time.sleep(3)
    print("HELLO FROM THREAD 1")
    
def greet1():
    time.sleep(5)
    print("HELLO FROM THREAD 2")
def greet2():
    print("HELLO FROM THREAD 3")
t1=threading.Thread(target=greet)
t1.start()

t2=threading.Thread(target=greet1)
t2.start()
t3=threading.Thread(target=greet2)
t3.start()
t1.join()
t2.join()

print("Main program ended")
