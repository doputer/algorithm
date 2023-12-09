n, m = map(int, input().split())

sites = {}

for _ in range(n):
    url, password = input().split()
    sites[url] = password

for _ in range(m):
    url = input()
    print(sites[url])
