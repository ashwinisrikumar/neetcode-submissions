class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1

        
        """
        $10
                [] * 11
        1
        2
        3
        ..
        10

        1, 5, 10
        12

        1, 5, 10

        1 = 1
        2 = 1 + 1 = 2
        3 = 1 + 1 + 1 = 3
        4 => 4
        5 => 1 + 1 + 1 + 1 + 1 = 5 or  5 = 1
        6 => 6 or  5 +1 = 2
        7 = 7 or 5 + 2 = 3
        8 = 8 or 5 + 3 = 8
        9 = 9 or 5 + 4 = 9
        10 = 10 or 5 + 5 = 6 or 5 = 2 or 10 = 1
        12 = 10 + 2 =3

          number of ways to reach 5 coin with 1 ruppee coin
            = 1 + number of ways to reach 5 - 1 = 4

        [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3]

        1. sum total -> if I include or if I exclude
        2. sum total -> sum of previous path ways
        
        
        number of ways for 12 rs
          = min(
              number of ways using only 1,
                    12 -> 11 -> 10 -> .... 1

              number of ways using 1 and 5,
                    12 -> 7 -> 2 -> 1
              number of ways using only 5,
              number of ways using  only 10
              )


        for val in range(1, amount + 1):   # 1, 2, 
            for c in coins:
                val - c >= 0: # 1 - 1 >= 0
                    dp[val] = min(dp[val], 1 + dp[val - c])

        """
        