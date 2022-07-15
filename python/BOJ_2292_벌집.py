# https://www.acmicpc.net/problem/2292 
# 등차수열 이라고 생각하면 되네 
# 1 7 19 37 61 
# 13 --> 3
# 58 --> 5 

n = int(input()) 
a_num = 1 #  1부터 시작, 
ratio = 6 
cnt = 1     

while a_num < n :  
    a_num += ratio * cnt
    cnt += 1
print(cnt)

