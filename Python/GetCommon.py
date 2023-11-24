class Solution:
    def getCommon(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        if set1.isdisjoint(set2) is True:
            return -1

        else:
            set1 &= set2
            return min(set1)