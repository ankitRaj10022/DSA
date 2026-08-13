class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt={}
        for num in nums:
            cnt[num]=cnt.get(num, 0)+1
            if cnt[num]>len(nums)//2: return num