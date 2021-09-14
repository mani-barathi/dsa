
def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr,start,end):
    pivot = end
    i = start - 1 

    for j in range(start,end):
        if arr[j] < arr[pivot]:
            i+=1
            swap(arr,i,j)

    i+=1
    swap(arr,i,pivot)
    return i

def quick_sort(arr,start,end):
    if start < end:
        fixed_index = partition(arr,start,end)
        quick_sort(arr,start,fixed_index-1)
        quick_sort(arr,fixed_index+1,end)


arr = [64, 34, 25, 12, 12, 22, 11, 90]
n = len(arr)
print(f"Before : {arr}")
quick_sort(arr,0,n-1)
print(f'After  : {arr}')
