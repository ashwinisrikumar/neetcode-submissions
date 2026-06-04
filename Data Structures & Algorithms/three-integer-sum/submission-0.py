class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index,element in enumerate(nums):
            if element>0:
                break
            if index>0 and element == nums[index-1]:
                continue
            left = index+1
            right = len(nums)-1

            while left <right:
                three_sum = element+ nums[left] + nums[right]
                if three_sum > 0:
                    right = right -1
                elif three_sum < 0:
                    left = left + 1
                else:
                    res.append([element,nums[left],nums[right]])
                    left = left + 1
                    right = right -1
                    while nums[left] == nums[left-1] and left<right:
                        left = left + 1
        return res
        
        



        
        