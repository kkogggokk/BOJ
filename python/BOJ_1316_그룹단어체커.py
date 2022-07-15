# 입력받으면 바로바로 체크하는 형태로 해보자. 

N = int(input())
result = N 

for _ in range(N):
    word = input()

    for i in range(len(word)-1):        # 인덱스 범위 에러를 피하기 위해 range 범위 확인 
        if word[i] != word[i+1]:        # 다른 문자를 입력받았을 경우 

            if word[i+1] in word[:i] :  # 다른 문자가 이전에 입력받은 문자인지 확인한다. 
                result -= 1             # 이전에 입력받은 문자가 있다면 그룹단어가 아니므로 입력받은 길이에서 -1 해준다. 
                break                   # 그룹단어가 아닌걸 확인했으니 멈추는게 효율적 
print(result)