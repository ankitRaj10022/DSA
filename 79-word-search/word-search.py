class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, sizeW = len(board), len(board[0]), len(word)
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#   lets create a helping function that helps to find that in which direction the all characters are for that to match the word and store them in
        def helper(row, col, index):
            if index==sizeW: return True
            visited[row][col] = True

            for dRow, dCol in directions:
                uRow, uCol = row+dRow, col+dCol
                if 0<=uRow<m and 0<=uCol<n and not visited[uRow][uCol]:
                    if board[uRow][uCol] == word[index]:
                        if helper(uRow, uCol, index+1): return True

            visited[row][col]=False
            return False


#   now iterate the indecies as normal to find the first letter of the word in the word
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(i, j, 1): return True


        return False
