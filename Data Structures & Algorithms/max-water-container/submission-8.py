class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        res = 0
        while l < r:
           curr_max  = min(heights[l],heights[r]) * (r-l)
           res = max(res,curr_max)
           if heights[l]<heights[r]:
            l = l+1
           else:
            r=r-1
        return res
        
        

