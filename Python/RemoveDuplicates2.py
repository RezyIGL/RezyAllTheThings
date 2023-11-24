class Solution:
    def removeDuplicates(self, nums: list) -> int:
        k = 0
        dictNums = {x: nums.count(x) for x in nums}

        for k in dictNums.keys():
            if dictNums[k] > 2:
                dictNums[k] = 2
                
        newArr = []
        
        for k, v in dictNums.items():
            for i in range(v):
                newArr.append(k)
        
        k = len(newArr)
        
        for n in range(k):
            nums[n] = newArr[n]
        
        return k
