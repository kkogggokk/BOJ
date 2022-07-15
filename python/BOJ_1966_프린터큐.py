# https://www.acmicpc.net/problem/1966 
# 인덱스를 구분해줘야 한다. 
N = int(input())

for _ in range(N): 
    n, m = map(int, input().split())         # m이 target 
    imp = list(map(int, input().split()))
    print_lst = list(zip([i for i in range(n)], imp))
    cnt = 0                                  # 출력순서 카운팅 변수 

    while print_lst :                        # print_lst가 없어지거나 break 만날 때까지 돌기
        max_value = max([print_lst[i][1] for i in range(len(print_lst))])
        
        if print_lst[0][1] == max_value:     # 리스트의 첫번째의 중요도값이 최대값인 경우 
            cnt += 1 

            if print_lst[0][0] == m :       # 첫번째가 target이 맞는지 확인하기 
                print(cnt)
                break
            else :
                print_lst.pop(0)            # 중요도 max인 첫번째 인덱스 pop해서 없애기
        else:                               # 리스트의 첫번째가 최대값이 아닌 경우 뒤로 이동한다.
            print_lst.append(print_lst.pop(0))