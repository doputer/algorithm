class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(reversed(a))
        b = list(reversed(b))

        if len(a) < len(b):
            a, b = b, a

        carry = 0

        for i in range(len(a)):
            t1 = int(a[i])
            t2 = int(b[i]) if i < len(b) else 0

            a[i] = (t1 + t2 + carry) % 2
            carry = (t1 + t2 + carry) // 2

        if carry:
            a += [1]

        return "".join(reversed(list(map(str, a))))
