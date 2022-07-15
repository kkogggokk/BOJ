# https://www.acmicpc.net/problem/2609 

'''
1. 둘의 최대 공약수를 구한다. 
    - 약수를 구한다. : 자연수를 어떤 수로 나누었을 때 나누어 떨어진다면, 그 수는 약수 
    - 공통되는 요소들을 저장한다(set)
    - 그중에서 가장 큰 것을 출력한다. 
'''
import math

def divisor(num): # 약수를 구해보자 
    divisor_list = [] 
    for i in range(1, int(math.sqrt(num)+1)): 
        if num % i == 0 : 
            divisor_list.append(i) 
            divisor_list.append(num//i)
    return sorted(divisor_list)


N, M = map(int, input().split())

# 각각의 약수를 구함 
n_divisor = divisor(N)
m_divisor = divisor(M)

# 각각의 약수를 구한 결과에서 공통된 부분 -  리스트 공통된 부분 찾기  --> 에서 최대값 : 최대공약수 (GCF:greatest common factor)
# https://hashcode.co.kr/questions/1193/%EB%91%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%97%90%EC%84%9C-%EA%B3%B5%ED%86%B5%EB%90%9C-%EC%95%84%EC%9D%B4%ED%85%9C%EB%A7%8C-%EC%B0%BE%EC%95%84%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%84-%EC%95%8C%EA%B3%A0-%EC%8B%B6%EC%96%B4%EC%9A%94 
GCF = max(list(set(n_divisor) & set(m_divisor)))
print(GCF)

# 최소공배수 Least Common Multiple: LCM
# N , M을 최대공약수로 나눠서 나온 몫 
n_mok = N // GCF 
m_mok = M // GCF 
LCM = GCF * n_mok * m_mok
print(LCM)


# dfsd