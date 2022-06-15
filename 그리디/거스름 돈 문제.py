n = int(input())
count = 0

# 큰 단위 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
for coin in array:
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
  n %= coin # 거슬러 주고 남은 돈

print(count)