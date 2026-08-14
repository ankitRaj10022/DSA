class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp, maxWater = 0, len(height)-1, 0
        while lp<rp:
            w = rp-lp
            h = min(height[lp], height[rp])
            currWater=w*h
            maxWater = max(maxWater, currWater)
            if height[lp]<height[rp]: lp+=1
            else: rp-=1  

        return maxWater