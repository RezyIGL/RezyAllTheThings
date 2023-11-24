class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        while sqrt*sqrt <= x:
            sqrt += 1
        return sqrt-1