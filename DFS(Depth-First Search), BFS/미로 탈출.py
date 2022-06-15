from collections import deque

def dfs(graph):
  Q = deque()
  Q.append((0,0))
  while Q:
    x, y = Q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(nx < 0 or nx >= n or ny < 0 or ny>= m): continue
      if(graph[nx][ny] != 1): continue
      graph[nx][ny] = graph[x][y] + 1
      Q.append((nx, ny))
  return graph[n-1][m-1]

n, m = map(int,input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = [list(map(int, input())) for _ in range(n)]
print(dfs(graph))
