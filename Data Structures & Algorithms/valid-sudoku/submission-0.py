class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      for row in range(9):
        seen = set()
        for i in range(9):
          if board[row][i] == ".":
            continue
          if board[row][i] in seen:
            return False
          seen.add(board[row][i])
      for col in range(9):
        seen = set()
        for i in range(9):
          if board[i][col]=='.':
            continue
          if board[i][col] in seen:
            return False
          seen.add(board[i][col])
      for square in range(9):
        seen = set()
        for i in range(3):
          for j in range(3):
            row = (square//3)*3+i
            col = (square%3)*3+j
            if board[row][col] == '.':
              continue
            if board[row][col] in seen:
              return False
            seen.add(board[row][col])
      return True





      """
      000000000
      000000001
      0000000110 

      rows = [set() for _ in range(9)] 
          rows[0] = {1,2,3}
          rows[1] = {4,5}

      cols = [0] * 9
      square  = [set() for _ in range(9)]
      
      r, c  => 2, 3   => 0
          (r // 3) *3  + (c//3)   -- 0 + 1 = 1
        
    rows = [0] * 9  -> 00000000
      1 << val  
          00100010
          00000010
          ========
          00000010

      0, 1 -> 1 row[0]
    cols = 000000000
    sq = 00000000


      row = [0] * 9    
          [
            [1, ., 2, ., 5, ., ....],
            []
          ]

          [
            10101
          ]

      cols = [0] * 9
      square = [0] * 9
      if row between 0 to 2 and col between 0 to 2 then square[0]
      if row beteen 3 to 5 and col between 0 to 2 then square[1]

      for each row
        for each col
          if . then continue

          bit = 1 << (int(row[r][c])) - 1

              0000000
              row[r][c] = 2
              0000010
              row[r][c] = 5
              0010000

              rows[r] = 1001000
              bit =     0001000
                        =======
                        0001000   != 0  -> False

              rows[r] = 1001000
              bit     = 0000100
                        =======
                        0000000  == 0  
              rows[r] = 1001100

              square_idex = [r // 3]*3 + [c // 3]
              row = 2, col = 3
              7,4
              6+1 -> index 7

              [1,., ., 4, ., ...]



      """