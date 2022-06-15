n, m = map(int, input().split())
arr = list(map(int, input().split()))

# def binary_search_left(array, target, start, end, on):
#   if start > end:
#     return -1
#   middle = (start + end) // 2
#   if array[middle] == target:
#     if on and middle > 0 and  array[middle - 1] == target:
#       return binary_search_left(array, target, start, middle - 1, on)
#     elif on == False and middle < n - 1 and array[middle + 1] == target:
#       return binary_search_left(array, target, middle + 1, end, on)
#     else: 
#       return middle
#   elif array[middle] < target:
#     return binary_search_left(array, target, middle + 1, end, on)
#   else:
#     return binary_search_left(array, target, start, middle - 1, on)
  
# left = binary_search_left(arr, m, 0, n - 1, True)
# right = binary_search_left(arr, m, 0, n - 1, False)

# if right-left == 0:
#   result = -1
# else:
#   result = right-left + 1
  
# print(result)

## bisect 이용 풀이

from bisect import bisect_left, bisect_right

# 값이 [left, right]인 데이터의 개수를 반환하는 함수
def count_by_range(arr, left, right):
  right_index = bisect_right(arr, right)
  left_index = bisect_left(arr, left)
  return right_index - left_index

count = count_by_range(arr, m, m)

if count == 0:
  print(-1)
else:
  print(count)
