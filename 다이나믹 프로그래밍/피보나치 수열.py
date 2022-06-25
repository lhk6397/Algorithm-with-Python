# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo_top_down(x):
  # 종료 조건(1 혹은 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  # 아직 계산 X라면 점화식에 따라 피보나치 결과 반환
  d[x] = fibo_top_down(x-1) + fibo_top_down(x-2)
  return d[x]

def fibo_bottom_up(x):
  # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
  d[1] = 1
  d[2] = 1
  
  for i in range(3, x + 1):
    d[i] = d[i-1] + d[i-2]
  return d[x]

print(fibo_top_down(99))
print(fibo_bottom_up(99))
