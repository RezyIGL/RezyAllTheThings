class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        leftP = 0
        rightP = 1
        returnVal = 0

        while rightP < len(prices):
            currProfit = prices[rightP] - prices[leftP]
            if prices[leftP] < prices[rightP]:
                returnVal = max(returnVal, currProfit)
            else:
                leftP = rightP
            rightP += 1

        return returnVal