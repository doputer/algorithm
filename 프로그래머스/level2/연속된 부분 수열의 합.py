def solution(sequence, k):
    answer = []

    interval_sum = 0
    end = 0
    gap = float('inf')

    for start in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1

        if interval_sum == k and end - start + 1 < gap:
            answer = [start, end - 1]
            gap = end - start + 1

            if gap == 1:
                return answer

        interval_sum -= sequence[start]

    return answer
