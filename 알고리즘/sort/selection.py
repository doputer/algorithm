def sort(A, n):
  for i in range(n - 1):
    largest = 0
    index = 0

    for j in range(n - i):
      if A[j] > largest:
        largest = A[j]
        index = j

    A[index], A[n - i - 1] = A[n - i - 1], A[index]
    print(A)


A = list(map(int, input().split()))

sort(A, len(A))
