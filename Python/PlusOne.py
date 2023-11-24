class Solution:
    def plusOne(self, digits):
        newArr = [str(x) for x in digits]
        temp = ""
        for n in newArr:
            temp += ''.join(n)

        temp = int(temp) + 1
        retArr = [int(x) for x in str(temp)]
        return retArr