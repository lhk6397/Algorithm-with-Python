n = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(n)]
arr = sorted(nodes, key=lambda x : (x[1], x[0]))
for x, y in arr:
  print(x, y)