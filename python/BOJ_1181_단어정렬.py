# https://www.acmicpc.net/problem/1181
'''
- (1 ≤ N ≤ 20,000) 입력갯수는 그렇게 크지는 않은것 같고 
- 주어지는 문자열의 길이는 50을 넘지 않는다. 이정도도 그렇게 큰거는 아니니까 
O(n^2)까지는 가능할듯 --> 그래도 최대한 빠르게 구현하는게 좋겠지? 
-  단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다. 

Q. n 갯수만큼 비교하기 위해서 단어를 저장해야하는데, 어떤 자료구조에 저장하면 좋을지? 
Q. 길이랑, 글자알파벳 순도 비교 정렬을 해야할텐데 정렬필터가 2가기 있다고 봐야지 

'''


# n = int(input())
# data_list = [input() for i in range(n)]
# # data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

# result = sorted(set(data_list))     # 중복을 제거 및 알파벳순으로 정렬한다.
# result.sort(key=lambda x: len(x))   # 정렬방식중에서 key로 정렬할수 있음 --> 람다함수 이용 
# for i in range(len(result)):
#     print(result[i])



# ---- version 02 
import sys
input = sys.stdin.readline

N = int(input())
l = []

for i in range(N):
    l.append(input().strip())

l = sorted(list(set(l)))
l.sort(key=lambda x : len(x))
print(*l)

