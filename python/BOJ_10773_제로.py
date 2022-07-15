# https://www.acmicpc.net/problem/10773 

'''
- 10만개 정도 값이 들어오니 메모리 관리 해주자.
- 가장 최근에 쓴 수를 지운다면 stack형태 자료구조이다.
- "0"값을 pop으로 처리하자 
- 결과는 sum으로 더해주자. 
'''

import sys 
K = int(sys.stdin.readline())
stack = []              # 메모리 관리차원에서 재할당 덜하기 위해서 미리 리스트를 만들어줌 

for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0 :       # num
        stack.pop()     # 이전에 들어온 값 없애기
    else : 
        stack += [num]  # append하면 메모리 재할당 된다고 어디서 들었던거 같아서 더해주는 형태로 함.

print(sum(stack))