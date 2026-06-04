class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum>target:
                r=r-1
            elif sum<target:
                l=l+1
            else:
                return [l+1,r+1]
        return []

        