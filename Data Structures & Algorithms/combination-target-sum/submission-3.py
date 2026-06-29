class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index,curr_comb,curr_target):
            if target == curr_target:
                res.append(list(curr_comb))
                return
            if index == len(nums) or curr_target>target:
                return
            curr_comb.append(nums[index])
            backtrack(index,curr_comb,curr_target+nums[index])
            curr_comb.pop()
            backtrack(index+1,curr_comb,curr_target)
        backtrack(0,[],0)
        return res
        