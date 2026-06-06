class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2 
        dp = [False] * (target + 1)
        dp[0]=True
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]=dp[j] or dp[j-num]
        return dp[target]

        """
        1,2,3,4
        target = 5

        1
            5  4 3 2 1

        2
           5 4 3 2

        3
            5 4 3

        0   1   2   3   4   5
        T   T   T   T   T   T


        1 2 3

        0   1   2   3
        T   T   F   T

        2 2 8
        target = 6

        0   1   2   3   4   5   6
        T   F   T   F   F   F   F


        """ 
        