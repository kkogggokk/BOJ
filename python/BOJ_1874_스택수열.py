# https://www.acmicpc.net/problem/1874 

import sys 

def solution(n):
    count = 0 
    stack = []
    result = []
    no_message = True 

    for i in range(0, n):
        x = int(input())

        while count < x : 
            count += 1 
            stack. append(count)    # 숫자 1부터 넣어주기 
            result.append("+")

        if stack[-1] == x : 
            stack.pop()
            result.append("-")
        else : 
            no_message = False
            break 

    if no_message == False:
        print("NO")
    else : 
        print(*result)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    solution(n)
