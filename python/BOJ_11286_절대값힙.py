# https://www.acmicpc.net/problem/11286

'''
- 가장 작은 수를 출력하는 것이므로 -> Priory Queue 이며, 이는 heapq를 통해서 구현할 수 있다. 
- 연산의 갯수가 10만개 이고 시간제한이 1초이므로 시간복잡도는 O(NlogN)수준이여야하는데..
- 절대값이작은값과, 입력된 수에서 가장 작은값을 구분해줘야 하는 부분이기때문에 여기서 어떻게 처리해줘야할지가 고민이다.... 
'''

import sys 
import heapq 
heap = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())           # x를 입력받기

    if x != 0 :                             # x가 정수 이면 lst에 값을 삽입한다. 
        heapq.heappush(heap, (abs(x), x))   # 절대값과 원본x값을 튜플 형태로 같이 입력하므로 절대값과 원본을 구분할 수 있다. 

    else :              
        try :                               # heap에 요소가 없는 상태에서 0을 입력받은 상태에서 heappop을 하게되면 에러가 발생한다.
            print(heapq.heappop(heap)[1])   # try - except 구문으로 예외를 처리해주자. 
        except:                             
            print(x)
            