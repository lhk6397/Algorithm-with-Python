import math

n = int(input())
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for _ in range(n + 1)]

# 에라토스테네스의 체 수행
for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True: # i가 소수인 경우(남은 수인 경우)
    # i를 제외한 i의 모든 배수 지우기
    j = 2
    while (i * j) <= n:
      array[i * j] = False
      j += 1

for i in range(2, n + 1):
  if array[i]:
    print(i, end=" ")