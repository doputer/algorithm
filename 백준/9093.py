t = int(input())

for _ in range(t):
  sentence = input().split()
  print(*list(map(lambda x: x[::-1], sentence)))
  
