class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]


        """

        0 -> 2
        0 -> 1 -> 2
        0 -> 2

        0 -> 3
        0 -> 1 -> 2 -> 3
        0 -> 1 -> 3
        0 -> 2 -> 3

        [0, 0, 0, 0]
        [0, 1, 2, 0]
        [0, 1, 2, 3]

        n = 5  
        [0, 0, 0, 0, 0, 0]
        [0, 1, 2, 0, 0, 0]
        [0, 1, 2, 3, 0, 0]
        [0, 1, 2, 3, 5, 0]
        [0, 1, 2, 3, 5, 8] -> 
            1, 1, 1, 1, 1
            1, 2, 1, 1
            1, 2, 2
            2, 1, 1, 1
            2, 2, 1
            
        at every step you calculate based on previous step
        each subsequent step you decide which of the previous steps you wan t o use

        memoization

        

        step 3 -> 


        """
