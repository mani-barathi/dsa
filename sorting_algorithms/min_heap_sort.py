# heap sort using min-heap can ony sort array in descending order

def heapify(arr,i,n):
    left  = (2 * i) + 1
    right = (2 * i) + 2
    smallest = i

    if left < n and arr[smallest] > arr[left]:
        smallest = left

    if right < n and arr[smallest] > arr[right]:
        smallest = right

    if smallest!=i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr,smallest,n)

def heap_sort(arr,length):
    # 1. heapify the array from the node above the leaf node till the root
    i = (length // 2) - 1
    while i >= 0:
        heapify(arr,i,length)
        i -= 1
    print("Heapified:",arr)    

    # 2. extract min and swap
    for i in range(length - 1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        # -3     90        90     -3
        heapify(arr,0,i)
        print(f"           {arr}")


arr = [64, 34, 11,-3, 90]
print(f"Normal   : {arr}")
heap_sort(arr,len(arr))
print(f'Sorted   : {arr}')

