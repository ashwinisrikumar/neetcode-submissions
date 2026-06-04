class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        left = 0
        right = 25
25-19/2
        mid = 12, 19, 21
        for p in piles:
            ceil(25 / 19) -> 2
            ceil(10/19) -> 1 
            ceil (23/19) -> 2
        ceil(2.3) -> 3
        floor(2.3) -> 2
        """
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            k = (l+r)//2
            totalTime = 0   
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <=h:
                    res = k
                    r=k-1
            else:
                    l = k+1
        return res

