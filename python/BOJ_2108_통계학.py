# https://www.acmicpc.net/problem/2108 
# https://wiki.jjagu.com/?p=209 
# https://daydreamx.tistory.com/entry/Baekjoon2108 

import sys
from collections import Counter # 최빈값 구하기 위해

def avg(arr):  
    return round(sum(arr)/len(arr))

def median(arr):    
    arr.sort()
    return arr[len(arr)//2]

def mode(arr):      
    #최빈값, 여러개 있을 때에는 최빈값 중 두번째로 작은 값을 출력한다. 
    counter = Counter(arr).most_common()
    if len(counter) > 1 and counter[0][1] == counter[1][1]:
        return counter[1][0]
    else : 
        return counter[0][0]

def scope(arr):     
    return (max(arr) - min(arr))

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)] 
arr = sorted([int(sys.stdin.readline()) for _ in range(N)]) # 애체로 정렬 해주는구나

print(avg(num))
print(median(num))
print(mode(num))
print(scope(num))

# 오잉? 시간초과라고 ? 
