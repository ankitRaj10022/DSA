class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        if len(nums) == len(set(nums)): return 0
        for num in set(nums):
            if nums.count(num)==2: res^=num
        return res