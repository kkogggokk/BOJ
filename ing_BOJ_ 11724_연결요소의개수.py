# https://www.acmicpc.net/problem/11724 

'''
0. 문제 분석하기 
    - 방향이 없는 그래프 = 양방향그래프 
    - 정점 N (1 <= N <= 1000)
    - 간선 M (0, <= M <= N(N-1)/2)
    - 간선의 양 끝점 u, v가 주어진다. 

1. 자료구조 및 알고리즘은 어떤거 ?
    - 연결요소를 구할 때 BFS, DFS 어떤걸로 선택해야하는지?  
    - u, v 를 양끝점으로 구분을 하고 있으니깐... 
    - deque로 연결해주는 형태로 저장하면 될것 같은데... 

2. deque로했을때 1-> 2 -> 5 -> 1 이런 경우는 어떻게 처리하지? 
- 2 ->{3, 4, 5} 
- 즉, 순환? 연결되는 경우 처리는 how ? 
'''

import sys 
from collections import deque

input = sys.stdin.readline

# N, M 입력받기 
# 근데, N, M 입려은 왜 받는거지? 이를 활용할 것도 있을텐데.. 
# M 은 M 번 반복할 수 있고....
N, M = map(int, input().split())

dq = deque()    

for _ in range(M): 
    # 간선의 양 끝점 u, v 입력받음 
    u, v = map(int, input().split())

    # u, v 가 deque에 있는지 여부를 확인 
    # 어렵다... ㅜㅜ 
