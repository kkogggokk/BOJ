# https://www.acmicpc.net/problem/2525

'''
[문제분석]
    - 끝나는 시간을 분 단위로 자동적으로 계산

[input]
    - 첫째줄, 현재 시각 시(0 <= A <= 23), 분(0 <= B <= 59)
    - 둘째줄, 요리하는 데 필요한 시간 C(0<=C<=1000) 

[output]
    - 

- 분에서 59를 넘어가면 -> 시+1 해주고, 00으로 돌아간다 
- 시에서 23:59분이 넘어가면 -> 0시 0분이 된다. 
'''
import sys 
input = sys.stdin.readline

hour, min = map(int, input().split())
time = int(input())
min += time 

while 60 <= min :
    min -= 60 
    hour += 1 
    if hour >= 24 : 
        hour = 0 

print(hour, min)