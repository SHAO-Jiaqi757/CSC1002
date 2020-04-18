import time 
import threading
def tick(n,name):
    for i in range(n):
        print("{}: {}".format(name,i))
        time.sleep(1)
t1 = threading.Thread(target = tick, args = (10, 't1'))
t2 = threading.Thread(target = tick, args = (15, 't2'))
t1.start()
t2.start()

t1.join()
print("t1 finished")

t2.join()
print("t2 finished")

