# Selection Sort
# Time Complexity => O(n^2)

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        index=i
        val = arr[i]
        for j in range(i+1,n):
            if arr[j]<val:
                index=j
                val = arr[j]
        arr[i], arr[index] = arr[index], arr[i]
    print(arr)

array = [3,5,1,6,8,7,4,2]
selectionSort(array)
