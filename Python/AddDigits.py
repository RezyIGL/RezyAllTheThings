from functools import reduce

class Solution:
    def addDigits(self, num: int) -> int:
        tempVar = [d for d in str(num)]

        while len(tempVar) != 1:
            tempVar = reduce(lambda x, y: int(x) + int(y), tempVar)
            tempVar = [d for d in str(tempVar)]
    
        return int(tempVar[0])