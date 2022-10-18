# threading library

import threading
import os

x = 0 

def increment() : 
	global x
	x += 1
	print("After increment of x with thread : ", x)

def handler(k) : 
	for i in range(1, 10000) : 
		increment()
		if i % 10 == 0 : 
		    print("thread is", threading.current_thread().name)


if __name__ == "__main__" : 
	t1 = threading.Thread(target = handler, args = (1,), name = 't1' )
	t2 = threading.Thread(target = handler, args = (1,), name = 't2')

	t1.start()
	t2.start()

	t1.join()
	t2.join()

