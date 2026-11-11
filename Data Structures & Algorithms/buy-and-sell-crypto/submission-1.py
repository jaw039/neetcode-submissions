class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low, sell high
        # meaning that selling must be after we buy it cant be before

        l = 0
        r = 1 
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1
        return maxP


