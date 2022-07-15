'''
- 원래 있는 리스트는 유지를 시켜줘야 N에 대한 인덱스를 옮겨가면서 출력을 할수 있는거니 N리스트는 유지하는게 좋을것 같음
- Out of Range Index에러가 발생하는 부분에 대해서 어떻게 처리할지에 대해서 고민을 해야할것 같다. 
- 포인트는 인덱스를 순환처럼 어떻게 구현할 것인가에 대한 부분인것 같다. 앞뒤 링크드 리스트처럼 구현을 해야하는 건데... 
    - itertools.islice 
        - end 지점이 없이 계속 로테이션을 하려면 어떻게 해야할까? deque를 생각해보긴했는데... 
        - shift하는 형태로 이동할수는 없나? deque를 뒤로 보낼생각을 못했네.. ㅜ 
'''

#import itertools
# for i in itertools.islice(range(N+1), K, 7, K):
#     print(i)

import sys 
from collections import deque

def solution(N, K):                 # 입력값 인자받기
    q = deque(range(1, N+1))
    result = []                     # 결과변수

    while q : 
        for i in range(K-1):        # 2칸씩 popleft 이동함 
            q.append(q.popleft())
        result.append(q.popleft())  # 3번째에 해당하는 element popleft하므로 제거 및 result에 넣어주기

    # print("<",end='')
    # print(*result, sep=", ", end=">")
    print('<'+str(result)[1:-1]+'>')
        
if __name__ == "__main__":
    N, K = [int(x) for x in sys.stdin.readline().split()]
    solution(N, K)
    