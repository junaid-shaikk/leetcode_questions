'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

#CODE:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=nums[0]
        curr_sum=0
        for i in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=i
            if max_so_far<curr_sum:
                max_so_far=curr_sum
        return max_so_far
      
      
