# binary search needs the array in a sorted manner
def binary_search(arr,first,last,search):
    if first > last:
        return -1

    mid=int((last+first)/2)
    if search == arr[mid]:
        return mid              

    if search < arr[mid]:
        return binary_search(arr,first,mid-1,search)

    if search > arr[mid]:
        return binary_search(arr,mid+1,last,search)
    return -1

# print(f'index  : {[n for n in range(0,10)]}')                 
# print(f'Array  : {arr}')

arr = [1, 5, -2, 104, 15, 7, 8]
search = 104

result = binary_search(arr,0,len(arr)-1,search)

if result == -1:
    print(f"{search} does'nt exists in the array")
else:
    print(f"{search} exists in the index {result}")
