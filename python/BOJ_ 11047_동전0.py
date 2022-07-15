# https://www.acmicpc.net/problem/11047

import sys 
    
input = sys.stdin.readline

N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)  # 큰단위부터 확인을 하기 위해서 내림차순 정렬한다. 
count = 0 

for coin in coins: 
    # if K == 0 :
    #     break
    count += K // coin 
    K = K % coin

print(count)

