import threading
import subprocess

class Ping:
    def __init__(self,host):
        self.host=host
    def __call__(self):
        result=subprocess.call(
            'ping -c2 %s &>/dev/null' % self.host,shell=True
        )
        if result ==0:
            print('\033[32m%s:up\033[om' % self.host)
        else:
            print('\033[31m%s:down\033[om' % self.host)


if __name__ == '__main__':
    ips=('176.19.1.%s'%i for i in range(1,255))
    for ip in ips:
        t=threading.Thread(target=Ping(ip))
        t.start()