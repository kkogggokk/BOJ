# https://www.acmicpc.net/problem/2798 
'''
김정인 버전 : 
- 양의 정수, 
- N장의 카드에 써져있는 숫자가 주어졌을때, 
- M을 넘지 않으면서 최대한 가까운 3장의 합을 구하기 
예)
입력 :5 21 
5 6 7 8 9 

출력 
21 = 6, 7, 8, = 5,8,9 = 

입력 
10 500
93 181 245 214 315 36 185 138 216 295

출력 
497 = 
'''



''' 
nCm --> 경우의수가  많이나오게됨 
M 에서 리스트의 가장 큰 수부터 하나씩 빼면서 값을 구해보는것도 좋을것 같아.
'''



#  for를 i, j, k로 3개 만들면.. n^3이니깐 진짜 비횰율적인데... 
# 파이썬 조합에 대한게 뭐가 없으려나.. 
# https://ourcstory.tistory.com/414 
# N , M = 10, 500 
# card_list = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]


from itertools import combinations
N, M = map(int, input().split())
card_list = list(map(int, input().split()))
sum_max = 0                                      # 더했을때 최댓값일 경우 변수 

select_3card = list(combinations(card_list, 3))  # 3장을 뽑은 경우의 수(다시 넣지 않는 상황)
for i in range(len(select_3card)):               # 모든 경우의 수를 확인해보자 
    temp = sum(select_3card[i])                  # 3장의 합에 대한 임시로 저장할 변수 
    if sum_max < temp <= M : 
        sum_max = temp 
print(sum_max)

    