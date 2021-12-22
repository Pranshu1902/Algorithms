# Odd-Even Sort
# Time Complexity => O(n^2)

def oddEvenSort(arr, n):
	isSorted = 0
	while isSorted == 0:
		isSorted = 1
		for i in range(1, n-1, 2):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				isSorted = 0
		for i in range(0, n-1, 2):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				isSorted = 0
	return


arr = [3,5,1,6,8,7,4,2]
n = len(arr)
oddEvenSort(arr, n)
print(arr)
