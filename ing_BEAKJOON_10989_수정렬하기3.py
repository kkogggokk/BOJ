# https://www.acmicpc.net/problem/10989 

# 입력하고 출력을 통해서 for를 2번 쓸수밖에 없는 구조인데... 
# 메모리를 최대한으로 줄일수 있는 방법이... --> 재할당을 없애는 형태로 진행하고 추가하는 형태로 
# https://wikidocs.net/21057  

import sys 

N = int(sys.stdin.readline())
lst = [0] * 10001 # 미리 리스트를 할당해줌 

for _ in range(N): 
    lst[int(sys.stdin.readline())] += 1 # 해당 인덱스에 input의 count된 값이 들어간다. 

for i in range(10001):
    if lst[i] != 0 : 
        for j in range(lst[i]):
            print(i)



