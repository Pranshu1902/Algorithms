# Bubble Sort (Sinking sort)
# Time Complexity => O(n^2)


arr = [3,2,4,6,8,1,5]
for i in range(len(arr)-1,-1,-1):
    for j in range(i):
        if int(arr[j]) > int(arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)