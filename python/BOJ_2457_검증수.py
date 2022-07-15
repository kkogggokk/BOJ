''''
- 컴퓨터 마다 6자리의 고유번호를 매김 
- 고유번호 첫5자리는 00000 ~ 99999 까지 수 중 하나 
- 6번째 자리에는 검증수가 들어간다. 
- 검증수는 고유번호의 처음5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지 
- 입력  : 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.
- 출력 : 검증수를 출력 
'''

'''
입력되는수가 1~5개이고, 검증수 1개 필요하니 
변수를 1~5를 넣어도 되긴할텐데 그래도 리스트를 활요하면 좋을듯함
리스트에서 각 값들 제곱가능? [i ** 2 for i in lst] 
# 파이썬 제곱 함수 : math.pow함수 
math.pow(x,y) : x의 y거듭제곱 
math.pow로 하니 실수로 표현이 되네 
'''

# 풀이1 . 
lst = list(map(int, input().split()))
print(int(sum([i ** 2 for i in lst]) % 10 )) # 끝에 int를 붙여줘야 runType에러가 발생안함 

#  풀이2. math.pow(x,y)를 사용해서 푸는 방법 
import math 
lst = list(map(int, input().split()))
print(int(sum([math.pow(i,2) for i in lst]) % 10))