# https://www.acmicpc.net/problem/1920 
'''
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다

둘다 10만개 입력값을 받으니까 --> sys로 인풋을 받아보도록 하자. 
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

https://leunco.tistory.com/56 <-- 참고 

'''

# import sys 

# N = int(sys.stdin.readline())
# N_list = [int(x) for x in sys.stdin.readline().split()] # 띄어서 입력을 받지만 리스트값으로 들어갈수있도록 하면 될듯 

# M = int(sys.stdin.readline())
# M_list = [int(x) for x in sys.stdin.readline().split()]

# for i in range(M):
#     if M_list[i] in N_list :
#         print(1)
#     else :
#         print(0)

# --> 이렇게 풀면 시간초과 발생 , 10만개 입력받는거 까지 생각해야할듯.. , 또 N_list, M_list로 에서 찾아내는 거면 n^2만큼 서칭해야하는거니 시간이 오래걸릴수밖에... 

# 입력을 받으면서 한번 해보자 
import sys
N = int(sys.stdin.readline())
N_list = set(int(x) for x in sys.stdin.readline().split())
M = int(sys.stdin.readline())
M_list = [int(x) for x in sys.stdin.readline().split()]

for i in range(M):
    if M_list[i] in N_list:
        print(1)
    else:
        print(0)

# ----
import sys
N = sys.stdin.readline()
A = set(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
M_num = list(map(int, sys.stdin.readline().split()))

for i in M_num:
    if i in A:
        print(1)
    else:
        print(0)
    
# ----
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')
