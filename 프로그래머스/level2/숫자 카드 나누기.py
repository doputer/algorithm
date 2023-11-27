from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    a = reduce(lambda prev, curr: gcd(prev, curr), arrayA, 0)
    b = reduce(lambda prev, curr: gcd(prev, curr), arrayB, 0)

    for i in arrayA:
        if i % b == 0:
            b = 0
            break

    for i in arrayB:
        if i % a == 0:
            a = 0
            break

    return max(a, b)
