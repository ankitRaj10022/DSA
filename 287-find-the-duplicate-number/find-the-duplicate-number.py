class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        for i in range(len(nums)):
            cnt=0
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]: cnt+=1
            if cnt>=1: return nums[i]
        '''

        '''
        seen=set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        '''


        s, f = nums[0], nums[0]
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f: break
        s=nums[0]
        while s!=f:
            s=nums[s]
            f=nums[f]
        return s