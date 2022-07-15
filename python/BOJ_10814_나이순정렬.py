#https://www.acmicpc.net/problem/10814 
# 나이(age), 이름(name) --> 나이가 증가하는 순, 
# 처리해줘야 하는 부분 --> 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서 
'''
if 나이가 같으면:
    입력된 순으로 확인 
'''
import sys 
input = sys.stdin.readline

class Solution():
    def sort_age(self):
        N = int(input())
        MEMBER = []
        for _ in range(N): 
            age, name = input().split()
            MEMBER.append([int(age), name])
        
        for i in sorted(MEMBER, key=lambda x :x[0]):
            print(i[0], i[1])

s = Solution()
s.sort_age()

