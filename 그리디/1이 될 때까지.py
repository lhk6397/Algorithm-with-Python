"""
문제 설명
어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행.
(단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능)
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

ex. N = 17, K = 4
1번 과정 수행 -> N = 16
2번 과정 2번 수행 -> N = 1
총 3번
17
수행해야 하는 과정의 최소 횟수 출력
"""

# N과 K가 충분히 작은 경우
'''
N, K = map(int, input().split())
count = 0

while N > 1:
  if N % K == 0: N /= K
  else: N -= 1
  count += 1

print(count)
'''

# O(logN) -> "가능하면 최대한 많이 나누는 작업"

n, k = map(int, input().split())

result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때  (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  result +=1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
