# https://www.acmicpc.net/problem/1436

'''
- 종말의 숫자 : 어떤수에 6이 적어도 3개 이상 연속으로 들어가는 수 
'''
N = int(input())
death_num = '666'
# print(death_num in '48999')
# print(death_num in '286666')
# print(death_num in '286166')
# print(death_num in '2866')

num = 0 # N까지 도달하기 위해서 세는 변수
result = [] 
# 그럼 N이 될때까지 count를 1씩 늘리면서 while문을 돌리고 도달하면  break로 멈추는 형태로 해야겠다. 
while True:
    num += 1 
    if death_num in str(num) : 
        result.append(num)
        if len(result) == N : 
            break 

print(result[-1])

