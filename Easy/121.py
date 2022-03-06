121.py

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# My Solution - Accepted

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) > 1:
            stock = 0
            stock_list = []
            
            left = prices[0]
            left_location = 0
            
            right = prices[1]
            right_location = 1

            if prices == sorted(prices, reverse=True):
                return 0

            for i in range(len(prices) - 1):
                if prices[i] > prices[(i+1)]:
                    if (prices[(i+1)] < left) and (i + 1) != len(prices) - 1:
                        left = prices[(i+1)]
                        left_location = (i + 1)
                else:
                    right = prices[(i+1)]
                    right_location = (i + 1)
                
                if left_location < right_location:
                    stock_list.append(right - left)

            stock = max(stock_list)
        else:
            return 0
        
        return stock

# Solution
"""
The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

Complexity Analysis

Time complexity: 
O(n) Only a single pass is needed.

Space complexity: 
O(1) Only two variables are used.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit


