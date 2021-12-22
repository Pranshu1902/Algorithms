# Counting sort

def countSort(arr):
	output = [0 for i in range(len(arr))]
	count = [0 for i in range(256)]
	ans = ["" for _ in arr]

	for i in arr:
		count[i] += 1
	for i in range(256):
		count[i] += count[i-1]
	for i in range(len(arr)):
		output[count[arr[i]]-1] = arr[i]
		count[arr[i]] -= 1
	for i in range(len(arr)):
		ans[i] = output[i]
	return ans

arr = [3,5,1,6,8,7,4,2]
ans = countSort(arr)
print(ans)
