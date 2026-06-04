class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxArea = 0
        while l<r:
            curr_area = min(heights[l],heights[r])*(r-l)
            maxArea = max(curr_area,maxArea)
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1
        return maxArea    
        