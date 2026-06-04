class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while (num+length) in numSet:
                    length +=1
                longest = max(length,longest)
        return longest



    """
    cache = set(nums)
    max_length = 0

    for each number
      if number - 1 is there in cache
         length = 1
         while number + length is there in cache
           max_length = max(max_length, length)


   {2,20,30,3,4,5}

   2 -> 4
   20 -> 1
   30 -> 1

    """
        