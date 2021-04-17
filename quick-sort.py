# Randomized quick sort is O(nlogn) with high probability. In-place.
# Tries to avoid the worst case of O(n^2) -> this case happens when the pivot is the largest element each time.
# And resulting height of tree is O(n). 
# That yields L of size n-1, E of size 1, G of size 0.
# If we divide the sequence almost equally with random pivot, the expected height of the tree is O(logn). Proof in algo book.
# And the time spent at each level is O(n), therefore we have O(nlogn).

import random
def inPlacePartition(L, start, end):
	randomIndex = random.randint(start,end)
	pivot = L[randomIndex]
	L[randomIndex], L[end] = L[end], L[randomIndex] # swap pivot with last index

	left = start
	right = end - 1
	while left <= right:
		while left  <= right and L[left] <= pivot: #find first item on left bigger than pivot
			left += 1
		while right >= left and L[right] >= pivot: #find first item on right smaller than pivot
			right -= 1
		if left < right:
			L[left], L[right] = L[right], L[left] #swap left(bigger) with right(smaller)
	L[left], L[end] = L[end], L[left] #put the pivot back in, thus serpating L in partitions of L,E,G

	return left

def inPlaceQuickSort(L, start, end):
	if start >= end:
		return
	middle = inPlacePartition(L,start,end)
	inPlaceQuickSort(L, start, middle-1)
	inPlaceQuickSort(L, middle+1, end)

def correctInPlaceQuickSort(L, start, end):
	while start < end:
		mid = inPlacePartition(L, start, end)
		if mid - start < end - mid:
			correctInPlaceQuickSort(L, start, mid - 1)
			start = mid + 1
		else:
			correctInPlaceQuickSort(L, mid + 1, end)
			end = mid - 1

L = [5,1,2,4,3,6,0,7,9,8]
print("Before sorting: ", L)
inPlaceQuickSort(L, 0, len(L) - 1)
print("After sorting: ", L)