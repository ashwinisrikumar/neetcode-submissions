class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index,curr_sub):
            if index == len(nums):
                res.append(list(curr_sub))
                return
            curr_sub.append(nums[index])
            backtrack(index+1,curr_sub)
            curr_sub.pop()
            backtrack(index+1,curr_sub)
        backtrack(0,[])
        return res
        