class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mySet = set()
        countS = [0] * 26
        countT = [0] * 26

        for c in s:
            countS[ord(c) - ord("a")] += 1

        for c in t:
            countT[ord(c) - ord("a")] += 1

        mySet.add(tuple(countS))
        mySet.add(tuple(countT))

        if len(mySet) == 1:
            return True
        
        return False