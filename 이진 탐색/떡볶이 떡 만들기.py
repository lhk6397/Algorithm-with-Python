n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = max(arr)

result = 0
while start <= end:
  middle = (start + end) // 2
  target = 0
  for x in reversed(arr):
    if x > middle: 
      target += x - middle
  
  if m > target:
    end = middle - 1
  else:
      result = middle
      start = middle + 1
      
print(result)
# middle 값은 시간이 지날수록 '최적화된 값'이 되기 때문에,
# 과정을 반복하면서 얻을 수 있는 떡의 길이는 합이 필요한 떡의 길이보다 크거나 같을 때마다 중간점을 기록하면 된다.