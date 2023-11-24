from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [1] * length
        prefix = 1
        postfix = 1

        for i in range(length):
            answer[i] *= prefix
            prefix *= nums[i]

            answer[length - i - 1] *= postfix
            postfix *= nums[length - i - 1]

        return answer