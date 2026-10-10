class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1,max(piles)
        res =r 
        while l<=r:
            mid = (l+r)//2
            rate_per_hr = 0
            for pile in piles:
                rate_per_hr += math.ceil(float(pile)/mid)
            if rate_per_hr<=h:
                res = mid
                r=mid-1
            else:
                l=mid+1
        return res