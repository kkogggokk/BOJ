# https://www.acmicpc.net/problem/7568

import sys 

N = int(sys.stdin.readline())  
peple_List = []     # 입력받는 사람마다 몸무게와 키를 저장할 변수 
result = []         # 결과를 담는 리스트

# 입력자체가 그렇게 크지 않아서 이중for를 써도 될것 같고, 
# 한번 위에 알려준 식대로 번호를 매겨보는 형태로 진행해보자. 

# 입력받기
for _ in range(N) : 
    weight, height = map(int, input().split())
    peple_List.append([weight, height])

# 이중for를 통해서 각각의 비교 
for i in peple_List:
    rank = 1                            # rank를 1로 초기화 
    for j in peple_List :                
        if i[0] < j[0] and i[1] < j[1]: # [0] 몸무게 비교, [1] 키비교 
            rank += 1                   # 상대방이 더 크면 +1 더한다. 
    result.append(rank)
    # print(rank, end =" ")             # 결과 저장하지 않고 바로 출력할 경우 

print(*result)