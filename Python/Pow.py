class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        if n<0:
            x = 1/x
            n = abs(n)

        while n:
            if n%2:
                p*= x
            x*=x
            n//=2
        return p