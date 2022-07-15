# https://www.acmicpc.net/problem/1712 

'''
- A만원 : 고정비용 (임대료, 재산세, 보험료, 급여 등 )
- B만원 : 가변비용 (재료비, 인건비)
- C만원 : 노트북가격 
- n : 생산 갯수 
- 총비용(total_price) = 고정비용 + 가변비용 
- 총수입(total_income) = C * n 
- 총수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(Break-even point)
- 손익분기점이 존재하지 않으면 -1을 출력한다. 

ex
- A = 1000, B=70 노트북 한대 생산하는 데 총 1070만원듦, 10대 생산 1700만원 , C = 170 --> 11 
- A = 3, B = 2, C = 1 --> -1 
- 2100000000 9 10 --> 2100000001

--> 구하면, 
'''
# 대략적으로 식 구해서 풀었음 


A, B, C = map(int, input().split()) 

try :
    break_even_point = int(A/(C-B)) + 1
    if break_even_point < 0 : 
        print('-1')
    else : 
        print(break_even_point)

except ZeroDivisionError:
    print('-1')


# 에? 런타임에러??? 런타임 에러 (ZeroDivisionError) --> 0으로 나누는 경우 에러가 발생한다.
# c-B 같은 값일 경우  
