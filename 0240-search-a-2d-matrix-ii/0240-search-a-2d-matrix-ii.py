class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        while col>=0 and row<len(matrix):
            if target == matrix[row][col]: return True
            elif target > matrix[row][col]: row+=1
            else: col-=1
        return False