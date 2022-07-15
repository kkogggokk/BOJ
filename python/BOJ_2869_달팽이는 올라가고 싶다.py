# https://www.acmicpc.net/problem/2869

'''
V : 나무막대의 높이 
A : 낮에 올라가는 높이 
B : 밤에 미끌어지는 길이 
day : 나무 막대를 모두 올라가려면 며칠이 걸리는지 구하라  

ex) A, B, V 순으로 입력된다. 
A*days - B(days-1) >= V 
A*days - Bdays + B >= V 
(A-B)days >= V - B
days >= (V-B)/(A-B)

2 1 5 ==> 4 = (2-1)+(2-1)+(2-1)+ 2 > 5
5 1 6 ==> 2 = (5-1)+ 5 > 6 
100 99 1000000000 ==> 999999901 = 


'''
A, B, V = map(int, input().split())
days = 0 # 초기값 
while True : 
    days += 1
    if (A * days - B*(days-1)) >= V : 
        break  
print(days)

# import sys 
# import math  
# A, B, V = map(int, input().split())
# print(math.ceil((V-B)/(A-B)))
