# heap sort using max-heap can ony sort array in ascending order

def heapify(arr,i,n):
    left  = (2 * i) + 1
    right = (2 * i) + 2
    largest = i

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,largest,n)

def heap_sort(arr,length):
    # 1. heapify the array from the node above the leaf node till the root
    i = (length // 2) - 1
    while i >= 0:
        heapify(arr,i,length)
        i -= 1
    print("Heapified:",arr)    

    # 2. extract max and swap
    for i in range(length-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,0,i)
        # print(f"           {arr}")


arr = [64, 34, 11,-3, 90]
print(f"Normal   : {arr}")
heap_sort(arr,len(arr))
print(f'Sorted   : {arr}')
