class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        l=0
        r=1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                max_so_far = max(max_so_far,profit)
            else:
                l=r
            r=r+1
        return max_so_far