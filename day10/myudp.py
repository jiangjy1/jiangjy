import os
import socket
import time

class Myudp:
    def __init__(self,host='',port='25836'):
        self.addr=(host,port)
        self.cust=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.custopt=self.cust.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.bind=self.addr

    def mainloop(self):
        while True:
            try:
                data, addr = self.cust.recvfrom(1024)
            except KeyboardInterrupt:
                print()
                break
            while True:
                pid=os.fork()
                if pid:
                    data.close()
                    while True:
                        result=os.waitpid(-1,1)[0]
                        print(result)
                        if not result:      #如果result值为0就break
                            break
                else:
                    self.cust.close()
                    while True:
                        # data = conn.recv(1024)
                        # if not data:
                        if data.strip() == b'quit':
                            break
                        sdata = '[%s] %s' % (time.strftime('%H:%M:%S'), data.decode('utf8'))
                        data.send(sdata.encode())
                        print(addr)
                    data.close()
                    exit()
        self.cust.close()

if __name__ == '__main__':
    cust=Myudp()
    cust.mainloop()


# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# print(s)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(('0.0.0.0',54321))
# # s.listen(1)
# # clock=strftime('%H:%M:%S')
# data,addr=s.recvfrom(1024)
# # print('Client connect from:',addr)
# # print(conn.recv(1024))        #接收套接字的数据
# data=data.decode('utf8')
# # data='[%s] %s' % (clock,data)
# data='hello'
#
# s.sendto(data.encode('utf8'),addr)
# s.close()