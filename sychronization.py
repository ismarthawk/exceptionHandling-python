import threading
lock = threading.Lock()


x = 0 


def increment(thread) :
    global x
    lock.acquire()
    x += 1
    print("x : ", x, "Thread : ", thread)
    lock.release()
    return 


def handler() : 
	for i in range(100) : 
		increment(threading.current_thread().name)


if __name__ == "__main__" :
    
    li = []
    for i in range(30) : 
        li.append(threading.Thread(target = handler, name =  'threa' + str(i + 1)))
    for i in li : 
        i.start()
        
    for i in li : 
        i.join()
    
    
    
    
    
    
    
    
    
    
# 	thread1 = threading.Thread(target = handler, name = 'thread1')
# 	thread2 = threading.Thread(target = handler, name = 'thread2')

# 	thread2.start()
# 	thread1.start()

# 	thread2.join()
# 	thread1.join()
