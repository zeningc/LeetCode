class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        i,j=n-1,0
        while i>-1 and j<m:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                i-=1
            else:
                j+=1
        return False
