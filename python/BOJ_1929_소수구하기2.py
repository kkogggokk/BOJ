def is_prime_number():
    import sys
    M,N = list(map(int, sys.stdin.readline().split()))


    sieve = [True] * (N+1)
    sieve[0] = False
    sieve[1] = False
    sqrt = int(N**0.5)
    for i in range(2, sqrt + 1):
        if sieve[i] == True:
            for j in range(i+i, N+1, i):
                sieve[j] = False

    targetList = [i for i in range(N+1) if sieve[i] == True]

    for i in targetList:
        if i >= M:
            print(i)



if __name__ == '__main__':
    is_prime_number()