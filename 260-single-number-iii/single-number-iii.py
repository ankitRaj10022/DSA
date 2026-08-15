class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            if nums.count(num)==1: res.append(num)
            if len(res)==2: break
        return res

        '''
        xall=0
        for num in nums:
            xall ^= num
        diff = xall & -xall
        a, b= 0, 0
        for num in nums:
            if num & diff: a^=num
            else: b^=num
        return [a,b]
        '''

