dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]
count = 0
st = input()

for char in st:
  if(char.isdigit()):
    y = int(char) - 1
  else: x = ord(char) - 97

for i in range(len(dx)):
  nx = x + dx[i]
  ny = y + dy[i]
  if(nx < 0 or nx >= 8 or ny < 0 or ny >= 8): continue
  count += 1

print(count)
