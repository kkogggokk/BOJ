from bisect import bisect_left, bisect, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)

tree = bisect_right(v, 3) - bisect_left(v, 3) 
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'number of 3 : {tree}') # 2 
print(f'number of 4 : {four}') # 4
print(f'number of 6 : {six}') # 6 