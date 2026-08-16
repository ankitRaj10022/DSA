class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a, b, n = 0, 0, len(grid)

        #repeating number
        seen=set()
        for row in grid:
            for num in row:
                if num in seen: a=num
                seen.add(num)
        

        #missing number
        currSum=0
        total=n*n #because of 2D matrix
        actSum= total*(total+1)//2
        for num in seen:
            currSum+=num
        b = actSum-currSum

        return [a,b]