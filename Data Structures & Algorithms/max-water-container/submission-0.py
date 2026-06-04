class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res=0
        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            res=max(res,area)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return res




        
        """
        2, 2, 2
              |
        |  |  |
        |  |  |

        area = (2 - 0) * min(2,3) = 2 * 2 = 4

        aea = (2 - 1) * min(2,3) = 1 * 2 = 2

        [1,7,2,5,4,7,3,6]

        area = (7 - 0) * min(1, 6) = 7
        area = (7 - 1) * min(7,6) = 6 * 6 = 36
        arae = (6 - 1) * min(7, 3) = 5 * 4 = 20
        """

        