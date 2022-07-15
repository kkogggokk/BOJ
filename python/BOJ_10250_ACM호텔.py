# https://www.acmicpc.net/problem/10250
# 정문에서 가장 짮을 거리에 있는 방 배정 
'''

규칙을 찾아본다면, H W N을 입력받았을 때 
--> N을 H로 나눴을때 
    - 나머지가 존재하지 않을때 딱 떨어질때 --> (H)(몫) 형태가 된다. 
    예시 ) 6 12 12 --> 602 
    예시 ) 30 50 90 --> 3003 
    - 나머지가 존재할때 -->(나머지)는 floor이되고 , (몫+1) 한 값이 num이 된다.
    예시 ) 6 12 10 --> 402 
    예시 ) 30 50 72 --> 1203 
    
- 몫+1 한 값의 범위는 1<= 몫+1 <= W 이어야 한다. 
- YY : 층 (Floor)
- XX : 번호 (Num)
라고 변수를 선언한다면, XX = 몫+1 이때 2자리이되 0으로 채워넣는다. 
'''

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())

    floor = N % H        # 나머지은 floor가 된다. 
    room_num = N // H    # 몫이 num이 된다.

    if floor == 0 : 
        print(str(H)+str(room_num).zfill(2))
    else:
        print(str(floor)+str(room_num+1).zfill(2))

