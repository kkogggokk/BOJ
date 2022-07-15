# https://www.acmicpc.net/problem/1065
'''
한 수 : 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한 수 라고 한다. 
N이 주어졌을때, 1보다 크거나 같고, N보다 작거나 같은 1 <= a <=  N  
결과 : 한수의 개수를 출력하는 프로그램을 작성 
    - cnt로 갯수를 하나씩 추가하는 형태
    - 리스트로 받아서 flag로 확인하는 방법도 괜찮을것 같고. 
'''

# 우선 한수를 만드는 것부터 하고 -> 함수로 만들어서 구현해보자. 
# N = [i for i in range(1, (int(input())+1))]
N = int(input())
cnt = 0 # 한수의 개수를 출력하는 변수 

for n in range(1,N+1) : 
    # 각자리수를 구한다. 
    print(list(map(int, str(n))))