class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        for i in range(len(nums)):
            cnt=0
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]: cnt+=1
            if cnt>=1: return nums[i]
        '''


        seen=set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
