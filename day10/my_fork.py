import os

# print('hello world')

# # os.fork()       #fork会生成一个子进程，一次fork返回两次，父进程执行一次，子进程执行一次
# pid=os.fork()
# if pid:
#     print('hello from parent')
# else:
#     print('hello from child')
# print('hello from both')

for i in range(2):
    pid=os.fork()
    if not pid:
        print('hello')
        exit()      #每次循环后要结束子进程，否则子进程会再生成子进程
