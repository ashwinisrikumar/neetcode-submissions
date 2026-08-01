class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max_so_far = 0

        while l < r:
            curr_q = min(heights[l],heights[r]) * (r-l)
            max_so_far = max(max_so_far,curr_q)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return max_so_far