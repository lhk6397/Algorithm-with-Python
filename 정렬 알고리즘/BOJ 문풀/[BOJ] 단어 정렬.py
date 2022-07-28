import sys
arr = []
n = int(sys.stdin.readline())
for _ in range(n):
  arr.append(sys.stdin.readline().strip())
arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))
for i in arr:
  print(i)