class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [0]*n
        l = [0]*n
        r = [0]*n
        l[0]=r[n-1]=1
        for i in range(1,n):
            l[i] = nums[i-1]*l[i-1]
        for i in range(n-2,-1,-1):
            r[i]= nums[i+1]*r[i+1]
        for i in range(n):
            res[i]=l[i]*r[i]
        return res
        
