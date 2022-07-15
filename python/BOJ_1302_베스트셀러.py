import sys
from collections import defaultdict

def solution(N):# 입력값 인자받기
    title = defaultdict(int)

    for i in range(N): 
        key = input().lower()
        title[key] += 1

    # 딕셔너리의 max값을 가진 키들을 추출해보자. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
    lst = [key for key, value in title.items() if value == max(title.values())]
    result = sorted(lst)
    print(result[0])

if __name__ == "__main__":
    # 입력값 넣어주기 
    N = int(sys.stdin.readline())
    solution(N)
    



