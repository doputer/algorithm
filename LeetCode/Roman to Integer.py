class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        romanInt = 0
        temp = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s):
                if roman[s[i]] > roman[s[i + 1]]:
                    romanInt += roman[s[i]] + temp
                    temp = 0
                elif roman[s[i]] < roman[s[i + 1]]:
                    romanInt += roman[s[i + 1]] - (roman[s[i]] + temp)
                    temp = 0
                    i += 1
                else:
                    temp += roman[s[i]]
            else:
                romanInt += temp + roman[s[i]]

            i += 1

        return romanInt
