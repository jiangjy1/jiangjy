import os
import subprocess

def ping(host):
    result=subprocess.call(
        'ping -c2 %s &>/dev/null' % host,shell=True
    )       #result的结果就是ping命令的$?
    if result == 0:
        print('%s up' % host)
    else:
        print('%s down' % host)


if __name__ == '__main__':
    alist=('176.19.1.%s' %i for i in range(1,255))
    for ip in alist:
        pid=os.fork()
        if not pid:
            ping(ip)
            exit()