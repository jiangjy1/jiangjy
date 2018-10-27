import os
import threading
import subprocess
import time

def ping(host):
    # print(time.localtime())
    result=subprocess.call(
        'ping -c2 %s &>/dev/null' % host,shell=True
    )       #result的结果就是ping命令的$?
    if result == 0:
        print('%s up' % host)
    else:
        print('%s down' % host)
    # print(time.localtime())

if __name__ == '__main__':
    ips=('176.19.1.%s'%i for i in range(1,255))

    for ip in ips:
        t=threading.Thread(target=ping,args=(ip,))        #创建工作线程
        t.start()       #线程开始执行，
