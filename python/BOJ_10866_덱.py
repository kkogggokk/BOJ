import sys 
from collections import deque

def push_front(x):
    D.appendleft(x)
    return D

def push_back(x):
    D.append(x)

def pop_front():
    if not D : 
        return -1 
    else: 
        return D.popleft()
    
def pop_back():
    if not D : 
        return -1 
    else : 
        return D.pop() 

def size():
    return len(D)

def empty():
    return 0 if D else 1

def front(): 
    if not D : 
        return -1 
    else : 
        return D[0]

def back():
    if not D : 
        return -1 
    else : 
        return D[-1]

N = int(sys.stdin.readline())
D = deque()

for i in range(N): 
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front": 
        push_front(cmd[1])

    elif cmd[0] == "push_back":
        push_back(cmd[1])

    elif cmd[0] == "pop_front": 
        print(pop_front())

    elif cmd[0] == "pop_back": 
        print(pop_back())

    elif cmd[0] == "size":
        print(size())

    elif cmd[0] == "empty": 
        print(empty())

    elif cmd[0] == "front": 
        print(front())

    elif cmd[0] == "back":
        print(back()) 

