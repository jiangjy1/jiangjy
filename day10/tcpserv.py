import os
import socket
import time

class TcpTimeServ:
    def __init__(self,host='',port=23232):
        self.addr=(host,port)
        self.serv=socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)
    def mainloop(self):
        while True:
            try:
                conn,addr=self.serv.accept()
            except KeyboardInterrupt:
                print()
                break
            pid=os.fork()
            if  pid:
                conn.close()
                #一个waitpid只能处理一个僵尸进程，多个子进程需要循环
                #waitpid优先处理僵尸进程，然后再处理非僵尸进程
                while True:
                    result=os.waitpid(-1,1)[0]  #检测到子进程不为0，子进程已经结束，处理掉子进程。子进程为0，不处理
                    print(result)
                    if not result:      #如果result值为0就break
                        break
            else:
                self.serv.close()
                while True:
                    data=conn.recv(1024)
                    # if not data:
                    if data.strip()==b'quit':
                        break
                    sdata='[%s] %s' % (time.strftime('%H:%M:%S'),data.decode('utf8'))
                    conn.send(sdata.encode())
                    print(addr)
                conn.close()
                exit()
        self.serv.close()


if __name__ == '__main__':
    serv=TcpTimeServ()
    serv.mainloop()
