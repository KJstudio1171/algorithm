def heapSwap(j, arr, i, len):
	if arr[j] < arr[2 * i - 1]:
			arr[j], arr[2 * i - 1] = arr[2 * i - 1], arr[j]
	if (2 * i) < len and arr[j] < arr[2 * i]:
		arr[j], arr[2 * i] = arr[2 * i], arr[j]

def makeHeap(arr, len):
	i = len // 2
	while i >= 1:
		j = i - 1
		while (j >= 0):
			heapSwap(j, arr, i, len)
			if j == 0:
				break
			j //= 2
		i -= 1

def heapSort(arr, len):
	if len == 0:
		return
	arr[0], arr[len - 1] = arr[len - 1], arr[0]
	makeHeap(arr, len - 1)
	heapSort(arr, len - 1)
	
arr = [1, 2, 3, 5, 7, 8 ,9 ,10]
makeHeap(arr, len(arr))
heapSort(arr, len(arr))
print(arr)