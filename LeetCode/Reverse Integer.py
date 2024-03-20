class Solution:
    def reverse(self, x: int) -> int:
        sign = 1

        if x < 0:
            sign = -1
            x *= -1

        ans = int("".join(reversed(str(x))))

        if ans > 2**31 - 1:
            return 0

        return ans if sign == 1 else -ans
