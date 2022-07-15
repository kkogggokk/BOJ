# https://www.acmicpc.net/problem/11050

'''
k < 0: 0
0 <= k <= n : (n k) = n! / k!(n-k)! 
k > n : 0 
5 2 = 5! / 2!(3)!

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=junhyuk7272&logNo=222053814549

팩토리얼을 구하는 걸 함수를 만드는게 좋을듯 : https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python 
--> 참고해서 

'''
import math 

n, k = map(int, input().split())
result = 0 

if k < 0 or k > n: 
    result = 0 
else : 
    result = int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

print(result)