def dfs(numbers, target, total, index):
  if len(numbers) == index:
    if total == target:
      return 1
    return 0

  ans = 0

  ans += dfs(numbers, target, total + numbers[index], index + 1)
  ans += dfs(numbers, target, total + numbers[index] * -1, index + 1)

  return ans


def solution(numbers, target):
  return dfs(numbers, target, 0, 0)
