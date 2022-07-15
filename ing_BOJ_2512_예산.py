# https://www.acmicpc.net/problem/2512 


N = int(input())
req = list(map(int, input().split()))
M = int(input()) # total

# 파라메트릭 서치를 하기 위해서 탐색 범위를 설정한다. (lo, hi, mid)
lo = 0
hi = max(req)
mid = (lo + hi) // 2 
ans = 0     # 답을 갱신해줄 변수 선언

def is_possible(mid):
    '''
    각 지방에 예산 상환선(mid)할당 시 총합이 초과하는지 아닌지를 확인하는 함수이다. 
    요청금액(req에서 개별을 의미하는 r)과 상환선(mid)중 작은값으로 설정하여 리스트의 합이 M(총합)보다 작거나 같아야 한다. 
    '''
    return sum(min(r,mid) for r in req) <= M

# 탐색 범위를 절반씩 줄이는 이분탐색을 반복한다. 
while lo <= hi : 
    # print(f'lo : {lo}, mid : {mid}, hi : {hi}, ans : {ans}')
    if is_possible(mid):    
        # 상환선(mid)값으로 설정 시 가능하다면 범위를 증가해줘야하니 lo는 +1해서 증가하고, ans는 상환값으로 저장한다. 
        lo = mid + 1        # 상환선 늘리고 
        ans = mid 
    else :
        # 상환선(mid)값이 불가하다면 범위를 낮춰야 한다. 
        hi = mid -1 
    mid = (lo + hi) // 2 
print(ans)
