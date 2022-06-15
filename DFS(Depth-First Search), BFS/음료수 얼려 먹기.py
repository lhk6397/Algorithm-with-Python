from collections import deque

# BFS 메소드 정의
# def bfs(n, m, graph, visited):
#   count = 0
#   for i in range(len(graph)):
#     for j in range(len(graph[i])):
#       if visited[i][j] or graph[i][j] == '1': continue
#       queue = deque([(i, j)])
#       # 현재 노드를 방문 처리
#       visited[i][j] = True
#       queue.append((i, j))
#       # 큐가 빌 때까지 반복
#       while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         cur = v
#         for dir in range(4):
#           nx = cur[0] + dx[dir]
#           ny = cur[1] + dy[dir]
#           if (nx < 0 or nx >= n or ny < 0 or ny >= m): continue
#           if (visited[nx][ny] or graph[nx][ny] == '1'): continue
#           queue.append((nx, ny))
#           visited[nx][ny] = True
#       count += 1
#   return count
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# n, m = map(int, input().split())
# graph = [input() for _ in range(n)]
# visited = [[False]*m for _ in range (n)]
# count = bfs(n, m, graph, visited)
# print(count)



# 나동빈 코드

def dfs(x, y):
  if x<=-1 or x>=n or y<=-1 or y >=m: return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0 :
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int ,input())))
  
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1
      
print(result)