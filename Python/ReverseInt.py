class Solution:
    def reverse(self, x: int) -> int:
        minR = -2**31
        maxR = 2**31 - 1

        x = str(x)

        if x[0] == "-":
            x = "-" + x[:0:-1]

        else:
            x = x[::-1]

        if minR > int(x) or int(x) > maxR:
            return 0

        return int(x)