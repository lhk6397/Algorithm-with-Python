# 동, 북, 서, 남
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]
direction = { 'D' : (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
# 입력
n = int(input())
dirs = list(input().split())
x,y = (0, 0)
for next in dirs:
  nx, ny = tuple(sum(elem) for elem in zip((x, y), direction[next]))
  if(nx >= n or nx < 0 or ny < 0 or ny >= n): continue
  x = nx
  y = ny

print(x+1, y+1)
