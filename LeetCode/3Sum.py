class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        a, b, c = [], [], []

        for n in nums:
            if n > 0:
                a.append(n)
            elif n < 0:
                b.append(n)
            else:
                c.append(n)

        aa, bb = set(a), set(b)

        if c:
            for i in aa:
                if -i in bb:
                    ans.add((-i, 0, i))

        if len(c) >= 3:
            ans.add((0, 0, 0))

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if -(a[i] + a[j]) in bb:
                    ans.add(tuple(sorted((a[i], a[j], -(a[i] + a[j])))))

        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                if -(b[i] + b[j]) in aa:
                    ans.add(tuple(sorted((b[i], b[j], -(b[i] + b[j])))))

        return ans
