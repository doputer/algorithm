def sort(A, n):
  for i in range(n - 1):
    for j in range(i + 1):
      if A[i - j + 1] < A[i - j]:
        A[i - j + 1], A[i - j] = A[i - j], A[i - j + 1]

    print(A)


A = list(map(int, input().split()))

sort(A, len(A))
