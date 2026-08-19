class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i, j =0, 0
        for num in nums:
            i = (i^num) & ~j
            j = (j^num) & ~i
        return i