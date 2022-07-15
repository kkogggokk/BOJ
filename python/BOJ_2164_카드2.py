# https://www.acmicpc.net/problem/2164 

# 우선 그냥 구현을 해봐야하나, 근데 입력자체가 50만개를 입력받기 때문에 다 구현하기에는 아마 "시간초과" 나올것 같아서 
# 규칙성이 있을것 같은데.... 



''' 
규칙성 
1) n = 짝수인  경우 
    STEP1) 길이가 <= 2 될때 까지 짝수 인덱스를 지운다
    STEP2) 길이가 <= 2 인 경우, 마지막 값을 선택한다. 

2) n = 홀수인 경우 --> 인덱스에 대한 규칙성이... ㅜㅜ 
    - 인덱스에 대한 규칙성이...

규칙성 구하는게 쉽지않네... ㅜ.ㅜ  
'''

import sys
N = int(sys.stdin.readline())
arr = [i+1 for i in range(N)]

while len(arr) > 1 : 
    if len(arr) % 2 :       # 길이가 홀수인 경우 
        t = [arr[-1]]       
        t.extend(arr[1::2])  
        arr = t 
    else :                  # 길이가 짝수인 경우
        arr = arr[1::2]

print(arr[0])