# https://www.acmicpc.net/problem/24416 

'''
피보나치수를 재귀 호출과 동적프로그래밍으로 구할 수 있다. 
각각의 실행횟수 출력하기 

'''

# def fib(n): # 재귀호출 
#     if n == 1 or n == 2 :
#         return 1 
#     else :
#         return fib(n-1) + fib(n-2)

def fibonacci(n):   
    # fibonacci_cnt = 0         # n-2로 DP로 구현 시 실행횟수 구할 수 있어서 주석처리, 직접 구현하고 싶다면 해제
    cache = [-1] *  (n+1)       # 리스트로 구현하기 위해서 
    cache[1] = cache[2] = 1     # 문제의 슈도코드와 맞추기 위해서 인덱스1,2에 값 넣어줌
    for i in range(3,n+1):
        # fibonacci_cnt += 1 
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]             # 
    # return fibonacci_cnt

n = int(input())
print(fibonacci(n), n-2)



# 재귀함수와 동적프로그래밍 통해서 함수는 만듦 -> 갯수는 어떻게 세지? 
# 재귀호출하면 카운트를 어디다가 넣어주지? 카운트 변수를 사용하지 않아도 재귀함수에서 수만큼 돌기때문에 카운드 변수를 사용하지 않아도 된다. 
# 동적프로그래밍에서 갯수 세기 

# omg... 시간초과... 어디서? 왜????/ 재귀함수를 사용하기 때문에
# 따라서 어차피 재귀함수를 사용해서 나오는 값자체가 n번째 해당하는 값이기 때문에 -> 카운트를 사용해서 풀기보다는 그 값을 출력해주면 될것 같고, 
# 


# 방법은 그렇다 -> 
'''
우선, 동적프로그래밍으로 피보나치를 구하는 함수를 구현한다. 
(1) 피보나치 함수의 리턴을 n번째 해당하는 값으로 리턴하는 경우 
    - print(fibonacci(n), n-2) # 왜 n-2? 전체길이 중 인덱스 1,2 가 빠지기 때문에 

(2) 피보나치 함수의 cnt를 구한는 값으로 리턴하는 경우 
    - print( , fibonacci(n))
'''