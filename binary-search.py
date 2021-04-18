'''
T  = O(logN)
S for iter = O(1)
S for recur = O(logN) -> used by stack memory, for langauges (Python) that don't support tail recurison optimization.
S for recur = O(1) for langauges that support tail recursion optimization.


----WHAT IS TAIL RECURSION?----
Same subroutine call performed as the final action of a precedure.
It is only important that the calling function return immediately after the tail call.
----WHY IS THIS IMPORTANT?----
With tail recursion optimization, the compiler can optimize memory.
Tail calls can be implemented without adding a new stack frame to the call stack.
Most of the frame of the current procedure is not needed, and can be replaced by frame of new tail call. 
Since the recursive call is the last statement, there is nothing to do in the current function,
so saving the current functions stack frame is no use.

Look at link for difference between the two types of factorial for use of tail recursion.
https://www.geeksforgeeks.org/tail-recursion/
'''
def recur_binary_search(L, target_val, low, high):
    if high >= low:
        #median_index = (low + high) // 2
        #use the following to prevent overflow
        median_index = low + (high - low) // 2
        if L[median_index] == target_val:
            return median_index
        elif L[median_index] < target_val:
            return recur_binary_search(L, target_val, low, median_index - 1)
        else:
            return recur_binary_search(L, target_val, median_index + 1, high)
    else:
        return -1

def iter_binary_search(L, target_val, low, high):
    while high >= low:
        #median_index = (low + high) // 2
        #use the following to prevent overflow
        median_index = low + (high - low) // 2
        if L[median_index] == target_val:
            return median_index
        elif L[median_index] < target_val:
            low = median_index + 1
        else:
            high = median_index - 1
    return -1

L = [0,1,2,3,4,5,6,7,8,9,10]
L_edge_case1 = [0]
L_edge_case2 = []

print("RECURSIVE BINARY SEARCH: ")
print("--NORMAL CASE: The list is ", L)
print("Find index of 5: ", recur_binary_search(L, 5, 0, len(L)-1))
print("Find index of 11: ", recur_binary_search(L, 11, 0, len(L)-1))
print("--EDGE CASE 1: The list is ", L_edge_case1)
print("Find index of 0: ", recur_binary_search(L_edge_case1, 0, 0, len(L_edge_case1)-1))
print("--EDGE CASE 2: The list is ", L_edge_case2)
print("Find index of something: ", recur_binary_search(L_edge_case2, 11, 0, len(L_edge_case2)-1))


print("\n\nITERATIVE BINARY SEARCH: ")
print("--NORMAL CASE: The list is ", L)
print("Find index of 5: ", iter_binary_search(L, 5, 0, len(L)-1))
print("Find index of 11: ", iter_binary_search(L, 11, 0, len(L)-1))
print("--EDGE CASE 1: The list is ", L_edge_case1)
print("Find index of 0: ", iter_binary_search(L_edge_case1, 0, 0, len(L_edge_case1)-1))
print("--EDGE CASE 2: The list is ", L_edge_case2)
print("Find index of something: ", iter_binary_search(L_edge_case2, 11, 0, len(L_edge_case2)-1))