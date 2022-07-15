# 시간초과... 
'''
2*n 까지 범위를 잡아두니까 이중포문때문인가 시간초과가 발생하네.. 
1 ≤ n ≤ 123,456 => 10만범위 수준이라면... 로그n 수준으로 나와줘야하는거...? 
그렇다면 

'''

import sys 
input = sys.stdin.readline

def is_prime_num(num):
    if num > 1 :
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0 :
                return False
        return True
    else :
        return False

while True : # 0입력 받으면 종료 
    n = int(input())
    result = []

    if n == 0 : 
        break

    for num in range(n+1, 2*n+1):
        if is_prime_num(num):
            result.append(num)
            
    print(len(result))
        




