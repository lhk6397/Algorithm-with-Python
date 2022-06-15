'''
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
'공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.

공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 했습니다.

최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보고 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

단, 1 <= N <= 100,000
입력 예시
5
2 3 1 2 2

출력 예시
2
'''

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
group_members = 0

for i in data:
  group_members += 1
  if group_members >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 # 총 그룹의 수 증가
    group_members = 0
  
print(result)