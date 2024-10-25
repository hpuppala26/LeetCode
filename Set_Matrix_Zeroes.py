class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = [0]*(len(matrix))
        zero_col = [0]*(len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row[i] = 1
                    zero_col[j] = 1
        print(zero_row, zero_col)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zero_row[i] == 1 or zero_col[j] == 1:
                    matrix[i][j] = 0
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
