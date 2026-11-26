import threading


def greet(name,age):
    print("Hello", name)
    print("This is age", age)

t1=threading.Thread(target=greet, args=("Aarav",17))
t1.start()
t1.join()
    