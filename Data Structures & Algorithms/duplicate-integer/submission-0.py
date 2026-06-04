class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1=[]
        for i in range(len(nums)):
            if nums[i] not in l1:
                l1.append(nums[i])
        if len(nums) == len(l1):
            return False
        else:
            return True
    

         