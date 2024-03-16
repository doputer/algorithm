class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        digits[-1] += 1

        while i > 0 and digits[i] > 9:
            digits[i] = 0
            digits[i - 1] += 1
            i -= 1

        return digits if digits[0] < 10 else [1, 0] + digits[1:]
