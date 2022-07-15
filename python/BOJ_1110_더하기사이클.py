# https://www.acmicpc.net/problem/1110

'''
- N : 0<= N <= 99 
- N은 str로 처리하는 게 좋을 듯 하다. -> 1, 0 일 경우 무한루프로 시간초과 뜬다. 
- int형태로 처리해야할 것 같다. 
- 흠.. 처음부터 자료구조를 잘못 선택한 경우인데.. 이게 구분이 되려나..? 
'''

N = int(input())
new_num = N
cnt = 0 

while True: 
    # tens = new_num // 10    # 십의 자리 , 10으로 나눴을 때 몫 
    # units = new_num % 10    # 일의 자리 , 10으로 나눴을때 나머지 
    tens, units = divmod(new_num, 10)
    new_num =  (units * 10) + ((tens + units) % 10)
    cnt += 1 

    if N == new_num :   # N과 새로운 수가 동일하면 멈춘다. 
        print(cnt)
        break 