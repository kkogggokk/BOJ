# https://www.acmicpc.net/problem/2480
'''
-  
'''
import sys 
input = sys.stdin.readline

A, B, C = map(int, input().split())
reward = 0 

if A == B == C : 
    reward = 10000 + A * 1000 
elif A == B or A == C :
    reward = 1000 + A * 100
elif B == C : 
    reward = 1000 + B * 100
else : 
    reward = max(A,B,C) * 100 

print(reward)

