class Solution:
    def searchInRow(self, mt: list[list[int]], target: int, row: int) -> bool:
        m = len(mt[0])
        s, e = 0, m-1
        while s<=e:
            mid=s+(e-s)//2
            if target==mt[row][mid]: return True
            elif target>mt[row][mid]: s=mid+1
            else: e=mid-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        srow, erow = 0 , m-1

        while srow <= erow:
            midrow = srow+(erow-srow)//2
            if target >= matrix[midrow][0] and target <= matrix[midrow][n-1]: return self.searchInRow(matrix, target, midrow)

            elif target > matrix[midrow][n-1]: srow = midrow+1
            else: erow = midrow-1

        return False