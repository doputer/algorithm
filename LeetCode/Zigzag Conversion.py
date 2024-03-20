class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = [""] * numRows
        i = 0
        d = -1

        for c in s:
            ans[i] += c

            if i == 0 or i == numRows - 1:
                d *= -1

            i += d

        return "".join(ans)
