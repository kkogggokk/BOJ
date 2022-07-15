# https://www.acmicpc.net/problem/2751
'''
리스트 sort로 하니 시간초과 뜨네.. 
https://assaeunji.github.io/python/2020-05-06-bj2751/


기본적인 sort들은 암기해두자 
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. --> 입력값이 100만이라서 시간복잡도를 logn 으로 진행해야함 

merge_sort해도 시간초과뜨네.. return때문인가? no --> merge_sort말고 다른걸로 해야할듯 
퀵소트로 한번 해보자, 흠 근데 nlogn
https://yuuj.tistory.com/5 --> pypy3로 해야하는 것과 input대신 sys로 하면 좀더 빨라짐 

ㅁ python은 느리고 pypy3는 통과되는 건 왜? 
ㅁ input이랑 sys로 하는거 차이 무엇?
ㅁ python으로 통과시킬수 있는 방법은 없는것? 

1. pypy3로 한번 해보자 
    - quick_sort --> 메모리초과 --> 어디서 메모리초과가 된거지? 
        - 퀵소트 코드 : 
            - https://www.daleseo.com/sort-quick/ --> 런타임에러 (뭐야이코드는왜 런타임에러야)
            - https://www.daleseo.com/sort-quick/ 일반코드:메모리초과 --> sys시도:메모리초과 /최적화코드:런타임에러
        - 퀵 공간복잡도 : 주어진 배열 안에서 교환(swap)을 통해, 정렬이 수행되므로 **O(n)**이다.
        - The space complexity of Merge sort is O(n). 
        - 퀵소트랑 멀지소트 공간복잡도가 같은 n인데 왜 ?? 이해가 안되네.. 어떤 부분에서 메모리 초과가 발생하는지? 코드에서 확인을 해봐도좋을것 같은데... 
        - 그럼 sys로 하면 어떻게 될지? 메모리초과
        - 백준 채점할때 어떤 예제에서 런타임 에러뜨는지 알고싶은데 크기때문인지 어떤 경우에 런타임 에러가 발생했는지에 대한 여부를 알수가 없으니.. 
    - merge_sort --> 통과   
        - 메모리, 시간 : 226208KB	1936ms
        - sys : 229536	1244  --> 시간이 많이 줄어듦 
    - 
2. 그렇다면 python으로 할수있는 방법은? 
- sys로 진행하니깐 됨. 대신 메모리 차이가 큼 
    - sys + merge_sort : 85776	7364 (메모리는 줄어듦, 시간은 많이걸림)
    - sys + 배열의 sort : 83508	1332 (<-- 이게 가장 최적인듯)

퀵으로 하니까 이해가 안되네.. 퀵으로 한번 해보고 싶은데... 퀵으로는 안되나보다.. 왜 안되는지.. ;; 
--> 이건 질문좀 해봐야겠다 커뮤니티에 

결론 
- 시간초과 발생할 경우, sys로 접근해보자 

'''

'''
# 백준 런타임에러 발생하는 경우 
1.배열에 할당된 크기를 넘어서 접근했을 때
2.전역 배열의 크기가 메모리 제한을 초과할 때
3.지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4.0으로 나눌 떄
5.라이브러리에서 예외를 발생시켰을 때
6.재귀 호출이 너무 깊어질 때
7.이미 해제된 메모리를 또 참조할 때
8. 프로그램(main 함수)이 0이 아닌 수를 반환했을 때
'''
# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1: # 재귀함수가 들어오기 때문에, 더이상 쪼갤수 없는 노드로 분할하기 위한 조건문 
		mid = len(arr)//2	# Finding the mid of the array

		# Dividing the array elements into 2 halves 
		L = arr[:mid]
		R = arr[mid:]
		
		mergeSort(L)	# Sorting the first half
		mergeSort(R)	# Sorting the second half

		# 각 노드의 인덱스를 하나씩 번갈아가며 값을 비교하기 위해서 처음에 0으로 초기화해준다. 
		# i : L 왼쪽노드 인덱스 ,  j : R 오른쪽 노드 인덱스 , k : arr 배열 인덱스 
		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]: 	# 왼쪽 노드값이 작으면
				arr[k] = L[i]	# arr[k] 값에 왼쪽 노드 값을 넣어준다
				i += 1			# 왼쪽 노드 인덱스를 1증가시킨다.
			else:
				arr[k] = R[j]	# 오른쪽 노드의 값이 작다면, arr[k]에 오른쪽 노드값을 넣어준다.
				j += 1			# 오른쪽 노드 인덱스를 1 증가시킨다.
			k += 1				# k인덱스 역시 1 증가 시킨다. 

		# Checking if any element was left
		# 왼쪽노드, 오른쪽 노드에 남은 요소들이 없는지 확인하는 부분이다. 
		while i < len(L): 
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

import sys 
ipt = sys.stdin.readline
nums = []

for i in range(int(ipt())):
    nums.append(int(ipt()))

mergeSort(nums)

for i in nums:
    print(i)
