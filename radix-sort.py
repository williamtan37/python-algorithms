''' 
For integers in Range 0-9
Space Complexity -> O(n + N). You store all n numbers and you have N buckets
Time Complexity -> O(n) + O(n + N). O(n) for first loop and O(n + N) second loop. Because you append n items
and visit N buckets.
Stable, not in place.
'''
def bucketSort(L):
	numberRange = 10 #0-9 aka number of buckets
	buckets = [[] for i in range(numberRange)]

	for num in L:
		buckets[num].append(num)

	result = []
	for i in range(numberRange):
		for num in buckets[i]:
			result.append(num)
	return result 

'''
Radix sort applies bucketSort D times from lower placeValue(ones) to higher placeValue(tens). 
D is the number of digits in the integer. 731 has 3 digits.
bucketSortForRadixSort -> 0 placeValue -> sorts by (Ones) placeValue. 
Stable sort, not in-place(uses auxiliary buckets)
Time Complexity -> O(D(n + N)). Because we repeat bucketSort D times.
Space Complexity -> O(n + N). For each iteration you store n numbers and have N buckets.
'''
def bucketSortForRadixSort(L, placeValue):
	numberRange = 10 #0-9 aka number of buckets
	buckets = [[] for i in range(numberRange)]

	for num in L:
		digitValue = (num // (10 ** placeValue)) % 10
		buckets[digitValue].append(num)

	result = []
	for i in range(numberRange):
		for num in buckets[i]:
			result.append(num)
	return result

def radixSort(L, numDigits):
	for i in range(0, numDigits):
		L = bucketSortForRadixSort(L, i)
	return L


L = [1,2,2,6,3,4,1,6,8,3,2,4,6,1,9,0,8,7,6,1,1,2]
print("Before bucket sort: ", L)
print("After bucket sort: ", bucketSort(L))
print()

L = [1,34,7,2,4,7,8,123,8,3,56,231,342,43,23,79,64,17,11,22,32,23,345,731,32,2,3,9,3,4,0]
print("Before radix sort: ", L)
print("After radix sort: ", radixSort(L, 3)) #the biggest integer here has 3 digits
