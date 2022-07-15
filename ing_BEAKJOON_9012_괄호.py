# https://www.acmicpc.net/problem/9012 

'''
-한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS
-주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 
-그 결과를 YES 와 NO 로 나타내어야 한다. 

풀이는 아래와 같다. 
입력값을 하나씩 받아 stack 리스트에 하나씩 넣을 것이다. 
짝을 이루면 pop하면서 stack의 길이에 따라 괄호여부를 판단하는형태로 진행한다. 
(가 오는 경우는 상관없지만 
)일 경우 조금 까다롭게 확인해야한다. 
    - stack이 비어있는지도 확인해야한다. 비어있지 않고 앞에 (이면 짝을이뤄 pop을 해준다.
    - )) 만 입력받는 경우  
'''


N = int(input())
for _ in range(N): 
    str = input()
    stack = []
    
    for i in str: # str값을 하나씩 확인하는 형태로 진행해보자 
        if i == '(' : 
            stack.append(i)
        elif i == ')': # )를 입력받았을 경우에는 조건이 필요하다 
            if len(stack) != 0 and stack[-1] == '(': # stack의 길이가 있고 앞의 값이 (이면 짝을 이루므로 pop하면서  
                stack.pop()
            else : # 
                stack.append(')')
                break 
    
    # stack의 길이로 여부를 판단한다.
    if len(stack) == 0 :    # 짝이 맞춰지면 pop하면서 없어지기 때문에 길이가 0이므로 YES이다. 
        print("YES")
    else:                   # stack의 길이가 남아있다면 짝을 이루지 못하므로 NO 이다. 
        print("NO")

