class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        srow, erow = 0, len(matrix)-1
        scol, ecol = 0, len(matrix[0])-1

        while(srow<=erow and scol<=ecol):
            for i in range(scol, ecol+1):
                res.append(matrix[srow][i])
            for j in range(srow+1, erow+1):
                res.append(matrix[j][ecol])
            for i in range(ecol-1, scol-1, -1):
                if srow==erow: break
                res.append(matrix[erow][i])
            for j in range(erow-1, srow, -1):
                if scol==ecol: break
                res.append(matrix[j][scol])
            
            srow+=1
            scol+=1
            erow-=1
            ecol-=1

        return res