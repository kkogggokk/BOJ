# https://www.acmicpc.net/problem/10828 

import sys 

def push(x):
    stack.append(x)

def pop(): # pop 할때 <built-in method pop of list object at 0x7f824fc83730> 이런식으로 출력하는 경우가 있음. 
    if (not stack) : 
        return -1 
    else : 
        return stack.pop() # pop 한후에 그 수를 출력해야한다. return 없이 stack.pop 할 경우 None이 뜨기 때문에 return 을 해줘야 한다. 

def size():
    return len(stack)

def empty(): 
    return 0 if stack else 1
    
def top():
    return stack[-1] if stack else -1 # 만약 스택이 존재한다면 stack[-1]을, 그렇지 않다면 -1을 

N = int(input())
stack = []

for i in range(N): 
    # push같은 경우는 변수를 2개 입력받고 , 나머지는 명령어만 입력을 받는다 이부분을 구분해줘야할 필요가 있다. 
    # sys.stdin.readline().rstrip().split() <-- 이부분을 몰랐네.. 
    input = sys.stdin.readline().rstrip().split()

    if input[0] == 'push':
        push(input[1])

    elif input[0] == 'pop':
        print(pop())

    elif input[0] == 'size':
        print(size())

    elif input[0] == "empty":
        print(empty())
        
    elif input[0] == 'top':
        print(top())
