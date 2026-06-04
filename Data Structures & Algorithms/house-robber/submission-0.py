class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        H1, h2, h3, h4

        rob -> h1 cannot h2
        rob -> h2 -> cannot h3

        h1 = nums[0]
        h2 = max(h1, nums[1])

        for i in range(2, len(nums)):1
            h = max(h1 + nums[i], h2)
            h2 = h1
            h1 = h
        return h1
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]

        