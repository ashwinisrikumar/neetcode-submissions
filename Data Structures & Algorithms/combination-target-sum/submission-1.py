class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i,len(nums)):
                if nums[j]+total>target:
                    return
                cur.append(nums[j])
                dfs(j,cur,total+nums[j])
                cur.pop()
        dfs(0,[],0)
        return res

        """
        2,5,6,9

        == 9

        baacktracking + dfs

        2 + 2 + 5

        1. Pick 2 -> [2,5,6,9] -> 2 -> [2,5,6,9] -> 2 -> 5th -> 10
        1. Pick 2 -> [2,5,6,9] -> 2 -> [2,5,6,9] -> 2 -> 5 == 9
        N-ary

        prune -> heuristic

        binary -> 2 child
        N-ary -> N childs

                2 out of 2,5,6,9

            2 out of 2,5,6,9    5   6   9t
        2   5   6   9
    2569
2569


        dfs 

            1
        2       3

    4       5 6     7

        def dfs(index, cur_list, cur_total):

            # base condition
            if cur_total == target:
                ans.append(cusr_list)
                return

            for i in range(index, len(nums)):

                curtotal + nums[i] > target:
                    return
                cur_list.append(nums[i])
                dfs(i, cur_list, cur_total + nums[i])     
                cur_list.pop()       




        """
        res = []
        nums.sort()
        



        