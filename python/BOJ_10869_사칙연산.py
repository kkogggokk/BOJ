# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

A, B = map(int,input().split())
if 1 <= A and B <= 10000 :
    print(A+B, A-B, A*B, A//B, A%B, sep = '\n')
