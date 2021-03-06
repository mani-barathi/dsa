
# when array only positive numbers
def counting_sort1(arr,n,r):
    # values in the arr represents the indexes in the count_arr 
    count_arr = [0 for _ in range(r)]
    output_arr = [None for _ in range(n)]

    for i in range(0,n):
        count_arr[arr[i]] += 1

    for i in range(1,r):
        count_arr[i] += count_arr[i-1]

    for i in range(0,n):
        count_arr[arr[i]] -= 1
        output_arr[count_arr[arr[i]]] = arr[i]
        
    for i in range(0,n):
        arr[i] = output_arr[i]

# when array has negative numbers
def counting_sort2(arr,n):
    min_element = min(arr)
    max_element = max(arr)
    r = max_element - min_element + 1
    count_arr = [0 for _ in range(r)]
    output_arr = [None for _ in range(n)]

    for i in range(0,n):
        count_arr[arr[i] - min_element] += 1

    for i in range(1,r):
        count_arr[i] += count_arr[i-1]

    for i in range(0,n):
        count_arr[arr[i] - min_element] -= 1
        output_arr[count_arr[arr[i] - min_element]] = arr[i]
        
    for i in range(0,n):
        arr[i] = output_arr[i]

arr1 = [1,4,1,2,7,5,2]
n1 = len(arr1)
r1 = 10          # range is between 0 and 9
print(f"Before : {arr1}")
counting_sort1(arr1,n1,r1)
print(f'After  : {arr1}')

print()

arr2 = [4,-1,-2,3,2,-2]
n2 = len(arr2)
print(f"Before : {arr2}")
counting_sort2(arr2,n2)
print(f'After  : {arr2}')
