# https://www.acmicpc.net/problem/2748 
# 1과 차이점은 n의 범위가 좀 더 넓음 

N = int(input())
cache = [-1] * 91   # 값을 좀 더 크게 잡아줌 왜? 
cache[0] = 0 
cache[1] = 1 

for i in range(2, N+1):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[N])