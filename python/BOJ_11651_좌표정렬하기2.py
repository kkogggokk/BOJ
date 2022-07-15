# https://www.acmicpc.net/problem/11651 
''' 
- 10만개 까지 입력값을 받으니 메모리 관리 해야한다. 
- y 값을 키로 정렬
'''

import sys

n = int(sys.stdin.readline())
XY = [] 

# XY = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 메모리를 더 많이 차지함 (재할당때문에?)
for _ in range(n): 
    x, y = map(int, sys.stdin.readline().split())
    XY.append([x, y])

result = sorted(XY, key=lambda x : (x[1], x[0]))

for x, y in result:
    print(x, y)