class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        n, cnt = len(nums), 0
        for i in range(n):
            total=0
            for j in range(i, n):
                total += nums[j]
                if total == k: cnt+=1
        '''

        cnt, curr_sum, seen = 0, 0, {0:1}
        for num in nums:
            curr_sum+=num
            if curr_sum-k in seen:
                cnt+=seen[curr_sum-k]
            seen[curr_sum]=seen.get(curr_sum, 0)+1

        return cnt