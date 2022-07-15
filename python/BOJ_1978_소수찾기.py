# https://www.acmicpc.net/problem/1978 

'''
- N : 수의 갯수 
- 
- 소수란? 1과 자기 자신만 있는 것 (1은 제외)
- 갯수를 출력하는 것이므로 count해주는 변수도 있으면 될것 같고. 
- 판별은 how? --> 2부터 자기자신까지 나눴을때 

# 생각보다 계속 틀려서 당황;;; 
'''

N = int(input())
nums = map(int, input().split())
cnt = 0 

for num in nums: 
    for i in range(2, num+1):
        if num % i == 0 :   # 2부터 num+1(자기자신까지)나눴을 때 0인 경우 중
            if num == i :   # 자긴 자신만 나눌수 있는 경우 
                cnt += 1 
            break           # 2부터 num+1(자기자신)까지 나머지가 있거나, 인수가 존재하는 경우로 조건에 해당하지 않음 --> 멈춤.
print(cnt)

