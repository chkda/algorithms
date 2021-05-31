"""
Leetcode Question no 53
Link: https://leetcode.com/problems/maximum-subarray/

Kadane's Algorithm

Time Complexity : O(n)
Space Complexity: O(1)

n : length of array
"""


def maxSubArray(nums):
    
    globalMaxSum = nums[0]
    localMaxSum = nums[0]

    if len(nums) == 1:
        return globalMaxSum

    for i in range(1,len(nums)):
        localMaxSum = max(nums[i],nums[i]+localMaxSum)

        if localMaxSum > globalMaxSum:
            globalMaxSum = localMaxSum

    return globalMaxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6)

