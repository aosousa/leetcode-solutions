class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                result = prices[r] - prices[l]
                if (result >= profit):
                    profit = result
            else:
                l = r
            r += 1

        return profit