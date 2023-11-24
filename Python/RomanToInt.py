class Solution:
    def romanToInt(self, s: str) -> int:
        myDict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        answerInt = 0

        for i in range(len(s)):
            if i < len(s) - 1 and myDict[s[i]] < myDict[s[i+1]]:
                answerInt -= myDict[s[i]]
            
            else:
                answerInt += myDict[s[i]]

        return answerInt 