# https://www.acmicpc.net/problem/2805 

import sys
def binary_search(start, end, M, tree_list):
    while start <= end : 
        mid = (start + end) // 2 
        cut_tree = 0 

        for tree in tree_list : 
            if tree >= mid : 
                cut_tree += tree - mid 

        if cut_tree >= M :
            start = mid + 1 
        else :
            end = mid -1 
    return end  

N, M = map(int, sys.stdin.readline().split()) 
tree_list = list(map(int, sys.stdin.readline().split()))
print(binary_search(0, max(tree_list), M, tree_list))


        




