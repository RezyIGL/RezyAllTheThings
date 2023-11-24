class Solution:
    def binSearchRec(self, nums, target: int, lo: int, hi: int):
        if lo > hi:
            return -1

        mid = (lo + hi) // 2

        if nums[mid] == target: return mid
        elif nums[mid] > target:
            return self.binSearchRec(nums, target, lo, mid-1)
        else:
            return self.binSearchRec(nums, target, mid+1, hi)

    def search(self, nums, target: int) -> int:
        if target > max(nums) or target < min(nums):
            return -1
        
        hi = len(nums) - 1
        return self.binSearchRec(nums, target, 0, hi)