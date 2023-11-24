class Solution:
    def intersect(self, nums1, nums2):
        retArr = []

        dict1 = {x: nums1.count(x) for x in nums1}
        dict2 = dict()

        for i in dict1.keys():
            dict2[i] = -1

        for i in nums2:
            dict2[i] = nums2.count(i)

        for k in dict1.keys():
            times = min(dict1[k], dict2[k]) if dict2[k] != -1 else -1
            for i in range(times):
                retArr.append(k)

        for i in retArr:
            if i == -1:
                retArr.remove(i)
        
        return retArr
