# https://www.acmicpc.net/problem/4949

import sys 

while True : 
    s = sys.stdin.readline().rstrip()
    stack = [] 

    if s == ".":
        break 

    for i in s : 
        if i == "(" or i == "[": 
            stack.append(i)
        
        # ")" 입력 시 CHECK 
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(")")
                break

        # "]" 입력 시 CHECK
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[" :
                stack.pop()
            else :
                stack.append("]")
                break
    
    # stack 잔여 여부(길이)에 따라 yes/no 결과 추출 
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
