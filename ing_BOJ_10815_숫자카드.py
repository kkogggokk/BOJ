# https://www.acmicpc.net/problem/10815 

import sys 
from bisect import bisect_left, bisect_right
input = sys.stdin.readline 

N = int(input())
N_lst = sorted(list(map(int, input().split())))              # 가지고 있는 숫자 카드. 찾는 대상 리스트로 이분 탐색을 위해 정렬이 되어야 한다.

M = int(input())
M_lst = list(map(int, input().split()))                      # 입력받은 카드가 가지고 있는지 없는지 여부를 확인

result = []
for i in M_lst:
    count = bisect_left(N_lst, i) - bisect_right(N_lst, i)  # 존재 여부를 갯수로 확인 
    if count:  
        result.append(1)
    else : 
        result.append(0)

print(*result, sep=" ")