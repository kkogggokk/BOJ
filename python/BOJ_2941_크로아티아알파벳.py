'''
- replace를 사용했을 경우 나타나는 이슈: 해당 글자를 ""공백으로 없애니 한번에 없어지면서 카운팅이 안됨. 따라서 글자수만큼 잘라내는 작업으로 해야할것같다. 

'''
# str = 'ljes=njak'
# str = "dz=ak"
# str = "c=c=" # replace할 경우 c= 한번에 다 없어지는 이슈발생 
# str = "ddz=z="

str = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0                         # 갯수를 세기위한 변수 

while str :                     # new_str 이 없어질때까지 반복하기 
    if str[0:3] in croatia:     # 앞에서 3글자가 있는 경우
        cnt += 1 
        str = str[3:]           # 글자 수 만큼 자르기 
        
    elif str[:2] in croatia:    # 앞에서 2글자가 있는 경우 
        cnt += 1 
        str = str[2:]
    
    else : 
        cnt += 1 
        str = str[1:]

print(cnt)