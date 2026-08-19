class Solution:
    def swap(self, nums, i, j) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start, end) -> None:
        while start<end:
            self.swap(nums, start, end)
            start+=1
            end-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot != -1:
            for i in range (len(nums)-1, pivot, -1):
                if nums[i]>nums[pivot]:
                    self.swap(nums, i, pivot)
                    break
        self.reverse(nums, pivot+1, len(nums)-1)
