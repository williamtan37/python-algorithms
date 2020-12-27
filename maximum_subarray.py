
import math
'''
Both use dynanmic programming. 
BUD = Bottleneck, unnessesary work, duplicates.

This one is:
Time: O(N), Space: O(N). 
Use the information gained from solving past steps to solve your current step because it is more efficient.
The max subarray ending at a given index is either the value at the index itself 
or it is the value at the index itself + the max subarray ending at the index before, depending on which is greater. 
At each step you are asking what is the max subarray ending at this index? 
Basically is a really smart way to compute a contigious subarray indirectly. Computing subarrays directly
will be less efficient. 
'''
def maxSubArrayLinearSpace(nums) -> int:
  cache = []
  for i in range(len(nums)):
    before = 0 if (i - 1 < 0) else cache[i - 1]
    extend = before + nums[i];
    result = nums[i] if nums[i] > extend else extend
    cache.append(result)
  return max(cache);


'''
Time: O(N), Space: O(1). 
In this implementation we dont use a list to keep track all biggest subarray values so the space is O(1).
'''
def maxSubArrayConstantSpace(nums) -> int:
  before, result = 0, -math.inf
  
  for i in range(len(nums)):
    extend = before + nums[i];
    before = nums[i] if nums[i] > extend else extend
    if result < before:
        result = before
  return result

L = [-2,1,-3,4,-1,2,1,-5,4];
print("Maximum Subarray of: ", L)
print("Using Linear space Linear time implementation: ", maxSubArrayLinearSpace(L));
print("Using Constant space Linear time implementation: ", maxSubArrayConstantSpace(L));