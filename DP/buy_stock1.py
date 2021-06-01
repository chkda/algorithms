"""
Leetcode Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Kadane's Algorithm

Time Complexity : O(n)
Space Complexity: O(1)

"""

def maxProfit(prices):

    max_profit = 0
    profit = 0

    for i in range(1,len(prices)):
        profit = max(profit + prices[i] - prices[i-1],0)
        max_profit = max(profit,max_profit)

    return max_profit

# print(maxProfit([7,1,5,3,6,4])==5)