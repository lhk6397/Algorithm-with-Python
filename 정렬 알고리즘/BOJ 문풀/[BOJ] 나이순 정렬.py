n = int(input())
nodes = [tuple(input().split()) for _ in range(n)]
arr = sorted(nodes, key=lambda x : x[0])
for x, y in arr:
  print(x, y)