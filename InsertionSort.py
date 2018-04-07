'''
INSERTION SORT IMPLEMENTATION:
'''

def i_sort(arr):
	for i in range(1, len(arr)):
		insert(arr, i, arr[i])

def insert(arr, pos, value):
	i = pos - 1
	while (i >= 0 and arr[i] > value):
		arr[i+1] = arr[i]
		i -= 1
	arr[i+1] = value

### Testing ###
arr = [4,2,1,4,6]
i_sort(arr)
print(arr)