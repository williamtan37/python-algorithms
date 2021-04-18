def swap(L, left, right):
    L[left], L[right] = L[right], L[left]

'''In-place, does not use extra memory, uses O(1) memory, no auxiliary data structure. not stable, does
not preserve relative order but it can be implemented as stable, if instead of swapping the minimum values 
is inserted into the correct position and elements are moved down.'''
def selection_sort(L):
    for target_index in range(len(L)-1):
        smallest_index = target_index
        for find_index in range(target_index+1, len(L)):
            if L[find_index] < L[smallest_index]:
                smallest_index = find_index
        swap(L, target_index, smallest_index)



L = [1,2,1,4,7,2,4,7,2,5,73,46,7,2,46,12]

print("Before sorting: ", L)
selection_sort(L)
print("After sorting: ", L)


''' Comparison to Insertion Sort WIKIPEDIA
Among quadratic sorting algorithms (sorting algorithms with a simple average-case of Θ(n2)), selection sort almost always outperforms bubble sort and gnome sort. 
Insertion sort is very similar in that after the kth iteration, the first k elements in the array are in sorted order. 
Insertion sort's advantage is that it only scans(**COMPARES) as many elements as it needs in order to place the k + 1st element, 
while selection sort must scan all remaining elements to find the k + 1st element.

Simple calculation shows that insertion sort will therefore usually perform about half as many comparisons as selection sort, 
although it can perform just as many or far fewer depending on the order the array was in prior to sorting. 
It can be seen as an advantage for some real-time applications that selection sort will perform identically regardless of the order of the array, 
while insertion sort's running time can vary considerably. 
***However, this is more often an advantage for insertion sort in that it runs much more efficiently if the array is already sorted or "close to sorted."***

While selection sort is preferable to insertion sort in terms of number of writes (Θ(n) swaps versus Ο(n2) swaps), 
it almost always far exceeds (and never beats) the number of writes that cycle sort makes, as cycle sort is theoretically optimal in the number of writes. 
This can be important if writes are significantly more expensive than reads, such as with EEPROM or Flash memory, where every write lessens the lifespan of the memory.

Finally, selection sort is greatly outperformed on larger arrays by Θ(n log n) divide-and-conquer algorithms such as mergesort. 
However, insertion sort or selection sort are both typically faster for small arrays (i.e. fewer than 10–20 elements). 
A useful optimization in practice for the recursive algorithms is to switch to insertion sort or selection sort for "small enough" sublists.
'''