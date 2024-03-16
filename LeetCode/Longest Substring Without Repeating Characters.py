class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = [[i, set(j)] for i, j in enumerate(s)]
        maximum = 0 if not h else 1

        while h:
            i, j = h.pop()

            if i + 1 < len(s) and s[i + 1] not in j:
                j.add(s[i + 1])
                h.append([i + 1, j])
                maximum = max(maximum, len(j))

        return maximum
