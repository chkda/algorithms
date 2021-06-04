"""
Leetcode Question: https://leetcode.com/problems/maximum-product-subarray/

Kadane's Algorithm

Time Complexity : O(n)
Space Complexity: O(1)

"""

def maxSubArray(nums):

    result = nums[0]
    maximum = nums[0]
    minimum = nums[0]

    for i in range(1,len(nums)):
        temp = maximum
        maximum = max(nums[i], nums[i]*maximum, nums[i]*minimum)
        minimum = min(nums[i], nums[i]*temp, nums[i]*minimum)
        result = max(result,maximum)

    return result

# print(maxSubArray([-2,-3,-1])==6)