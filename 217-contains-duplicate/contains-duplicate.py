class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num in seen: return True
            seen.add(num)
        return False