n = int(input())
count = 0
include_three = [3, 13, 23]
''' 
00시 00분의 경우: 15개 
00시의 경우: 15 * 60 = 900
3
13
23
43
53
30 ~ 39
15개

1800 - 225 = 1575개
3, 13, 23시의 경우: 60 * 60 = 3600
'''
# 내 풀이
if(n<3):
  count = 1575 * (n+1)
elif(n<13):
  count = 3600 + 1575 * n
elif(n<23):
  count = 7200 + 1575 * (n-1)
else:
  count = 10800 + 1575 * 21
  
print(count)

# 완전 탐색(Brute forcing): 00시 00분 00초 ~ 23시 59분 59초까지의 모든 경우는 86400가지

#h = int(input())
count2 = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count2 += 1
        
print(count2)