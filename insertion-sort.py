'''
In-place alogorithm, with sorted list on left and unsorted list on right.
Maintains sorted list on the left. Naturally, first index is already sorted.
From the unsorted list on the right, from index 1 to end, insert unsorted value into sorted list from the end of the sorted list.
This is done by, starting from the end of the sorted list, shifting values in the sorted list that are bigger than curr up by one index. This also overwrites curr.
Then insert curr in the empty spot in the sorted list resulting from the shifting.

Worst case is O(N^2).
Best case is O(N). That case is if the list is in reverse order.
'''

def insertionSort(L):
	for i in range(1, len(L)):
		curr = L[i]
		j = i - 1
		while j >= 0 and L[j] > curr:
			L[j+1] = L[j]
			j -= 1
		L[j+1] = curr


L = [5,1,2,4,3,6,0,7,9,8]
print("Before insertionSort: ", L)
insertionSort(L)
print("After insertionSort: ", L)

L = [5,7,3,2,10,9,4,2,5,6]
print("Before insertionSort (with duplicates): ", L)
insertionSort(L)
print("After insertionSort: ", L)

