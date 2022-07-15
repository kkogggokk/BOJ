import math 

def is_prime_number(num):
    if num > 1 :            # 예외처리 1,1 을 입력받았을 경우, 1은 소수가 아니다. 
        for i in range(2,int(math.sqrt(num))+1) :    # 범위를 제곱근으로 
            if num % i == 0 :     
                return False    # 소수가 아니다
        return True         # 소수  
    else :
        return False

M = int(input())
N = int(input())
result = [] # 결과를 담을 리스트 선언 

for num in range(M, N+1): 
    if is_prime_number(num): 
        result.append(num)

if result : 
    print(sum(result))
    print(min(result))
else : 
    print(-1)




