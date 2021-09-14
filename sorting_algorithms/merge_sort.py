
def merge(arr,start,m,end):
    i = start
    j = m + 1
    temp = [None for _ in range(start,end+1)]
    k = 0

    while i <= m and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1

    while i <= m :
        temp[k] = arr[i]
        i+=1
        k+=1

    while j <= end :
        temp[k] = arr[j]
        j+=1
        k+=1

    k = 0
    for s in range(start,end+1):
        arr[s] = temp[k]
        k+=1


def merge_sort(arr,start,end):
    if start < end:
        m = (start + end) // 2
        merge_sort(arr,start,m)
        merge_sort(arr,m+1,end)
        merge(arr,start,m,end)

arr = [64, 34, 25, 12, 12, 22, 11, 90]
n = len(arr)
print(f"Before : {arr}")
merge_sort(arr,0,n-1)
print(f'After  : {arr}')

