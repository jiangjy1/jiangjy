import os
import time

pid=os.fork()
if pid:
    print('in parent')
    print(pid)
    time.sleep(60)
else:
    print('in child')
    print(pid)
    time.sleep(15)      #子进程没有可执行代码，将会变成僵尸进程