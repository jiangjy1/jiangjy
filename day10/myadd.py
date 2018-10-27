import os
import time
import threading
# class Add:
#     def __call__(self):
def add():
    result=0
    for i in range(0,100000000):
        result+=i
    print(result)


if __name__ == '__main__':
    start=time.time()
    # add()
    # # add()
    for i in range(4):
        pid=os.fork()
        if not pid:
            add()
            exit()
    os.waitpid(-1,0)
    os.waitpid(-1,0)
    os.waitpid(-1,0)
    os.waitpid(-1,0)
    end=time.time()
    print(end-start)


    start=time.time()
    tlist=[]
    for i in range(2):
        a=threading.Thread(target=add())
        tlist.append(a)
        a.start()
    for t in tlist:
        t.join()
    end=time.time()
    print(end-start)


