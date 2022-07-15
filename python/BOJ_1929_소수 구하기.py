# https://www.acmicpc.net/problem/1929
# 시간초과 --> sys.stdin.readline 을 사용해보자 --> https://hooongs.tistory.com/131 --> M, N 해도 시간초과 발생함 
# 입력값이 1,000,000(백만) 이니까.. v_0.1같은 경우 for가 2개 있으므로 n^2되니까 --> 다른 형태로 진행해야할듯 어떻게 줄일수 있을까...  
# --> 기존의 코드를 함수로 했는데도 안됨 같은 문제. 
# https://gettingtoknowit.tistory.com/89 --> 에라토스테네스의 체? 2의배수, 3의배수 해당 배수를 지어주는 형태로 진행해야하는 구나 
# 그러면 소수 구하는 방법이 2가지 인거네 


''' v_0.1
import sys 
M, N = map(int, sys.stdin.readline().split())

for num in range(M,N+1):
    for i in range(2, num+1):
        if num % i == 0 :   # 2부터 num+1(자기자신까지)나눴을 때 0인 경우 중
            if num == i :   # 자긴 자신만 나눌수 있는 경우 
                print(num)
            break       
'''

import sys 
import math 

def isPrime(num): 
    if num == 1 : 
        False 
    else : 
        # 왜 제곱근인가? 소수가 아니면 1 2 4 // 1 2 3 6 //1 5 25 // 1 2 5 10 
        # 1 2 5 10, --> 10의 제곱근 3.*** -> 3이 넘어가므로 +1 범위까지 나눠주게되면 range(2,4) --> 10을 2, 3 로 나눴을때 2의 배수 혹은 3의 배수인지 확인이 된다. 
        # 1 5 25 --> 25의 제곱근 5 --> +1 범위까지 나눠주면 --> range(2,6) --> 25를 2, 3, 4, 5 의 배수인지 여부를 확인한다. 
        for i in range(2, int(math.sqrt(num)+1)):   # math.sqrt 제곱근을 하면 실수형이므로 int정수로 변환해줘야 한다 
            if num % i == 0 :                       # num을 제곱근으로 나눴을때 0이면 나눠진다는 의미이므로 소수가 아니다
                return False 
        return True 

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1): 
    if isPrime(i) :                                 # isPrime(i)가 소수이면 함수 리턴이 True이므로 프린트를 한다 
        print(i)

# 결과 : 32972KB	3720ms