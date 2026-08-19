class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ml, chs = 0, 0, 0, set()
        while r < len(s):
            if s[r] not in chs:
                chs.add(s[r])
                ml=max(ml, r-l+1)
                r+=1
            else:
                chs.remove(s[l])
                l+=1

        return ml