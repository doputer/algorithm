class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        ans = "0"
        sign = 0

        for c in s:
            if (c == "+" or c == "-") and not sign and len(ans) == 1:
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            elif str.isdigit(c):
                ans += c
            else:
                break

        ans = int(ans)

        if ans > 2**31 - 1:
            return 2**31 - 1 if sign >= 0 else -(2**31)

        return ans if sign >= 0 else -ans
