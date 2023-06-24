#LeetCode 121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        result = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                result = max(result, sell - buy)
            else:
                buy = sell
        return result