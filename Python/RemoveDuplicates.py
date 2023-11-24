class Solution:
    def removeDuplicates(self, nums: list) -> int:
        answ = sorted(set(nums), key=nums.index)
        k = len(answ)
        for i in range(k):
            nums[i] = answ[i]
        return k