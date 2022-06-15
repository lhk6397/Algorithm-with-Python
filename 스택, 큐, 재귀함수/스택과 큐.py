# 스택 -> 기본 리스트로 구현 가능
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
print(stack[::-1]) # 최상단 원소부터 츨력
print(stack) # 최하단 원소부터 출력

# 큐 -> deque을 이용하여 구현 
# 리스트를 이용할 수도 있으나 deque을 이용해야 시간 상의 이득
from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft() # 앞 원소 삭제

print(queue) # 먼저들어온 순서대로 출력
queue.reverse() # 역순
print(queue) # 나중에 등어온 원소부터 출력