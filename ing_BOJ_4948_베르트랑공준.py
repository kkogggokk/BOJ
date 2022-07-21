# 시간초과... 
'''
2*n 까지 범위를 잡아두니까 이중포문때문인가 시간초과가 발생하네.. 
1 ≤ n ≤ 123,456 => 10만범위 수준이라면... 로그n 수준으로 나와줘야하는거...? 
그렇다면 

'''

from cgi import test
import sys 
input = sys.stdin.readline

prime_num = []
for i in range(2, 123456*2):    # 전체 범위에서 소수를 먼저 구한다. 
    cnt = 0 
    for p in range(2, int(i**0.5)+1):
        if i % p == 0 : # 배수인 경우 
            cnt += 1 
            break 
    if cnt ==  0:       # 소수인 경우
        prime_num.append(i)

while True : # 0입력 받으면 종료 
    n = int(input())
    result = 0

    if n == 0 : # 0이 들어오면 프로그램 종료 
        break

    for i in prime_num:         # 미리 구한 소수에서 n범위에 해당하는 부분만 cnt 갯수를 센다. 
        if n < i <= 2*n:        
            result += 1 
    print(result)




import sys 

