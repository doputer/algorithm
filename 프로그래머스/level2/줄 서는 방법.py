from math import factorial


def solution(n, k):
    answer = []

    l = [i + 1 for i in range(n)]

    while n > 0:
        value = factorial(n - 1)

        answer.append(l[(k - 1) // value])
        l.pop((k - 1) // value)

        k %= value
        n -= 1

    return answer
