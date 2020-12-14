def merge(L1, L2):
	result = []
	i, j = 0, 0

	while i < len(L1) and j < len(L2):
		if L1[i] < L2[j]:
			result.append(L1[i])
			i += 1
		else:
			result.append(L2[j])
			j += 1

	if i < len(L1):
		result.extend(L1[i:])
	if j < len(L2):
		result.extend(L2[j:])
	return result

def merge_sort(L):
	if len(L) == 0 or len(L) == 1:
		return L
	else:
		mid = len(L) // 2
		return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

L1 = [2,1]
L2 = [5,6,7,3,4,2,3,5,2,3,4,1,9,10]
print("List before sort: ", L1)
print("List after sort: ", merge_sort(L1))

print("List before sort: ", L2)
print("List after sort: ", merge_sort(L2))