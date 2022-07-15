tall = sorted([int(input()) for _ in range(9)])     # 9명의 키를 입력받고 정렬한다. 
flag = False                # case 1개 출력 여부 플래그 

for i in range(8):          # range(9) 하게되면, 아래 j에서 인덱스 범위에 넘어가게 된다. 따라서 8로 지정한다.
    for j in range(i+1, 9): # range(9) 하게되면 같은 것을 뽑는 경우도 있으므로 i+1로 지정한다. 
        if sum(tall) - tall[i] - tall[j] == 100 : 
            for k in range(9) : 
                if i != k and j != k : 
                    print(tall[k])
            flag = True 
            break           

    if flag:                   # case 1회 추출하면 flag=True 이므로 반복문 탈출
        break 

                



# flag()  # 한번만 출력하기 위해서 함수로 출력하기