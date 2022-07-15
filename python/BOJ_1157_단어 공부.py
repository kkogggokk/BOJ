# https://www.acmicpc.net/problem/1157
# 대소문자로 된 단어 입력 --> 가장 많이 사용된 알파벳이 무엇인지 알아내기 
# 단, 대소문자 구분하지 않음 
# 가장 많이 사용된 알파벳이 여러개 존재하는 경우 ? 를 출력 


# 출력을 대문자로 출력해주니까 입력받을때 대문자로 변환을 해주자. 
# list.count('문자') --> 해당 문자의 갯수를 세어준다. 
# 딕셔너리로 key값을 중복되지 않은 문자로 지정해줘도 될듯 

s = input().upper()

keys = list(set(s))  
values = [s.count(keys[i]) for i in range(len(keys))]
di = dict(zip(keys, values))

if values.count(max(values)) >= 2 : 
    print("?")
else:
    print(max(di, key=di.get))
