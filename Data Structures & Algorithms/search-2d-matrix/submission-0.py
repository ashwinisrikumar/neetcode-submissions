class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in range(len(i)):
                if target == i[j]:
                    return True
        if j == len(i)-1:
            return False
        