class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum+=num
            maxSum = max(maxSum,curr_sum)
        return maxSum