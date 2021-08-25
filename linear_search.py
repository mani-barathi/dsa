import random

arr=list(range(1,11))
random.shuffle(arr)
search=random.choice(arr)


def linear_search(arr,search):
	for i in range(len(arr)):
		if arr[i]==search:
			print(f'{search} found at index : {i}')
			return
	print(f'{search} not exists in array')		


print(f'Array  : {arr}')
print(f'Search : {search}')
linear_search(arr,search)

