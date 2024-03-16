class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = list(strs[0])

        for i in range(1, len(strs)):
            if len(trie) > len(strs[i]):
                trie = trie[: len(strs[i])]

            for j, k in enumerate(strs[i]):
                if j < len(trie) and trie[j] != k:
                    trie = trie[:j]

        return "".join(trie)
