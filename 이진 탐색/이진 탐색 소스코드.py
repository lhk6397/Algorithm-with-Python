# Binary Search implement by recursion
def binary_search_recursion(array, target, start, end):
  if start > end:
    return None
  middle = (start + end) // 2
  if array[middle] == target:
    return middle
  elif array[middle] < target:
    return binary_search_recursion(array, target, middle + 1, end)
  else:
    return binary_search_recursion(array, target, start, middle - 1)

def binary_search_loop(array, target, start, end):
  while start <= end:
    middle = (start + end) // 2
    if array[middle] == target:
      return middle
    elif array[middle] > target:
      end = middle - 1
    else:
      start = middle + 1
  return None
      

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = map(int, input().split())

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_loop(array, target, 0, n-1)
if result == None:
  print("There is no target element")
else:
  print(result + 1)

