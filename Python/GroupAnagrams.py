from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        myDict = defaultdict(list) # my hashMap for anagrams

        for string in strs:
            
            count = [0] * 26 # from A to Z

            for char in string:
                count[ord(char) - ord("a")] += 1

            myDict[tuple(count)].append(string)

        return myDict.values()