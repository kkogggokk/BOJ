def tempFunc():
    import sys
    M,N = list(map(int, sys.stdin.readline().split()))


    TFList = [True] * (N+1)
    TFList[0] = False
    TFList[1] = False
    sqrt = int(N**0.5)
    for i in range(2, sqrt + 1):
        if TFList[i] == True:
            for j in range(i+i, N+1, i):
                TFList[j] = False

    targetList = [i for i in range(N+1) if TFList[i] == True]

    for i in targetList:
        if i >= M:
            print(i)



if __name__ == '__main__':
    tempFunc()