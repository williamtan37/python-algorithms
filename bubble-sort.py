'''
T = O(N^2), In-place, stable.
After every iteration, the largest value bubbles up to the right. In other words, 
a sorted list builds up on the right side. 
At each iteration of the unsorted left side, compare all adjacent values and swap them if out of order.
You run this N-1 times to build a completed sorted list, because one value falls in final place every iteration.
This algorithm is slightly optimized because you don't continue to bubble(swap) in the sorted partition.
However it is not fully optimized for the case that the list is already in sorted order. 
So we don't have the best case of O(N) here that bubble sort optimal has.
We would need to utilize a flag to catch this best case. Flag for no swaps were completed.
Nonetheless doesn't matter that much because it is still O(n^2) worst case and this is a bad sorting algorithm. 
https://youtu.be/Jdtq5uKz-w4   <-  describes everything about this aglo, including all optimizations of this algo.
'''

def swap(L, left, right):
    L[left], L[right] = L[right], L[left]

def bubbleSort(L):
	for timesToRun in range(1, len(L)):
		for i in range(0, len(L) - timesToRun):
			if L[i] > L[i+1]:
				swap(L, i, i+1)

def bubbleSortWithBestCaseLinear(L):
	for timesToRun in range(1, len(L)):
		flag = False
		for i in range(0, len(L) - timesToRun):
			if L[i] > L[i+1]:
				swap(L, i, i+1)
				flag = True
		if not flag:
			break


L = [1,2,1,4,7,2,4,7,2,5,73,46,7,2,46,12]

print("Before sorting: ", L)
bubbleSort(L)
print("After sorting: ", L)

L = [5,1,2,4,3,6,0,7,9,8]
print("Before sorting ", L)
bubbleSort(L)
print("After sorting: ", L)