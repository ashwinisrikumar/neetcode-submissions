class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        l=0
        r=1
        while r<len(prices):
            if prices[l]<prices[r]:
                cur_prof=prices[r]-prices[l]
                max_prof = max(cur_prof,max_prof)
            else:
                l=r
            r=r+1
        return max_prof

         