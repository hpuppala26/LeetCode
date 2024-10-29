class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if i!=j:
                    matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
                else:
                    continue
        for k in range(len(matrix)):
            matrix[k] = matrix[k][::-1]
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        
