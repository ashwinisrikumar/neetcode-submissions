class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        sum n numbers = n(n + 1) /2 => 3*4/2 = 6
        sum = 6
        missing = 0
         2*3/2 = 3
        sum = 2

        [1,2,3]

        res = 3
        3 + 0 - 1 + 1 - 2 + 2 - 3
        1-0 + 2-1 + 3-2 = 0

        """
        res = len(nums)
        for i in range(len(nums)):
            res += i-nums[i]
        return res
        