# https://www.acmicpc.net/problem/11650 

'''
- 점을 10만개 정도 받으니 sys로 입력값을 받도록하자, 
- 정렬을 하는거니, key를 통해서 정렬을 하면 될것같은데,
- (X,Y) 쌍을 이루는 거니 튜플형태로 입력을 받으면 될것 같은데 한번해봅시다.
'''

import sys 

N = int(sys.stdin.readline())
XY = []

for _ in range(N):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    XY.append([x,y])

for i in sorted(XY): 
    print(i[0], i[1])



# 클래스나 함수사용안했을때 --> 46128, 4544 
# 클래스와 함수사용했을때 --> 

# 이전 코드에서 클래스와 함수를 사용했을때 차이가 있을까? 메모리는 큰 차이 없고, 시간은 좀더 늘어났는데 시간은 왜지? 
# 람다 사용하지 않고 바로 sorted 해서 하니 메모리랑 시간 줄어듦 
# 