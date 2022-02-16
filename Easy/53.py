53.py

"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray



'''
Approach 1: Optimized Brute Force

Algorithm

Initialize a variable maxSubarray = -infinity to keep track of the best subarray. We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.

Use a for loop that considers each index of the array as a starting point.

For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the starting index, adding each element to currentSubarray. Every time we add an element it represents a possible subarray - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.

Return maxSubarray.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray


'''
Approach 2: Dynamic Programming, Kadane's Algorithm

Algorithm

1. Initialize 2 integer variables. Set both of them equal to the first value in the array.

    - currentSubarray will keep the running count of the current subarray we are focusing on.
    - maxSubarray will be our final return value. Continuously update it whenever we find a bigger subarray.

2. Iterate through the array, starting with the 2nd element (as we used the first element to initialize our variables). 
    For each number, add it to the currentSubarray we are building. 
    If currentSubarray becomes negative, we know it isn't worth keeping, so throw it away. 
    Remember to update maxSubarray every time we find a new maximum.

3. Return maxSubarray.
'''