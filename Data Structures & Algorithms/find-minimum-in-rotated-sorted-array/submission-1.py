class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]
        
        """
        target = 1
        1. left = 0
           right = 
        
           mid = 2

           if number is smaller then left or greater than mid
           then it is present in right side
            left = mid + 1
        else:
                right = mid - 1

            if number is smaller than mid or greater than right
            right = mid - 1
            else left = mid + 1

        """