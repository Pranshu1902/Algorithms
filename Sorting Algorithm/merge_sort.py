# Merge Sort
# Time Complexity => O(n*logn)

def merge(x,y):
    p1=p2=0
    out=[]
    while p1 < len(x) and p2 < len(y):
        if x[p1] < y[p2]:
            out.append(x[p1])
            p1+=1
        else:
            out.append(y[p2])
            p2+=1
    out += x[p1:] + y[p2:]
    return out

def mergeSort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))

arr = [3,5,1,6,8,7,4,2]
print(mergeSort(arr))
