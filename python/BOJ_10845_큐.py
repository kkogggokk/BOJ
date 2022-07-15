# https://www.acmicpc.net/problem/10845 
# 이전 스택이랑 너무 비슷함 --> 다른 방법으로도 풀어보자 



def push(x):
    que.append(x)

def pop():
    if (not que):
        return -1 
    else : 
        return que.pop(0)

def size():
    return len(que)

def empty():
    return 0 if que else 1 

def front():
    if (not que): 
        return -1
    else:
        return que[0]

def back():
    if (not que):
        return -1
    else : 
        return que[-1]


import sys 
N = int(sys.stdin.readline())
que = [] 

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        push(cmd[1])
    if cmd[0] == 'pop':
        print(pop())
    if cmd[0] == 'size':
        print(size())
    if cmd[0] == 'empty':
        print(empty())
    if cmd[0] == 'front':
        print(front())
    if cmd[0] == 'back':
        print(back())