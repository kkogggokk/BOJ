# https://www.acmicpc.net/problem/2231 

# M의 분해합이 N인 경우, M을 N의 생성자라한다. 
# 256(분해합N)의 생성자는 245(생성자M)이다. 
# 256 입력 --> 245 //256-2
# 216 입력 --> 198 
# 자연수 N의 가장 작은 생성자를 구해라. 큰 생성자도 있다는 이야기네 그럼? 
# 생성자가 없는 경우에는 0을 출력한다. 

N = int(input())
result = 0 

for i in range(1, N+1):
    A = list(map(int, str(i)))
    result = i + sum(A)

    if result == N : 
        print(i)
        break 
    
    if i == N : 
        print(0)