# Algorithm with Python

## "이것이 취업을 위한 코딩테스트다 with Python"

1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

- 알고리즘 성능 분석
  - N <= 500 -> O(N^3)까지
  - N<= 2000 -> O(N^2)까지
  - N<= 100,000 -> O(NlogN)까지
  - N<= 10,000,000 -> O(N)까지
- 유용한 표준 라이브러리

  - 내장 함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
  - itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공

    - 순열
    - 조합
    - 중복 순열
    - 중복 조합

  - heapq: 힙(Heap) 자료구조를 제공 -> for 우선순위 큐 구현
  - bisect: 이진 탐색(Binary Search) 기능을 제공
    - bisect_left, bisect_right
  - collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
    - counter: Iteralbe 객체가 주어졌을 때 내부의 원소가 몇 번 등장했는지 알려줌
  - math: 필수적인 수학적 기능을 제공
    - 최대공약수(GCD), 최소공배수(LCM)

1. 그리디 & 구현

1. DFS & BFS

- 스택 & 큐
- 재귀함수
- DFS & BFS

1. 정렬 알고리즘

- 선택 정렬
- 삽입 정렬
- 퀵 정렬
- 계수 정렬

1. 이진 탐색

- 순차 탐색과 이진 탐색
- 파라메트릭 서치(Parametric Search)
- bisect 라이브러리

1. 다이나믹 프로그래밍

- 다이나믹 프로그래밍 구현 방식
  - TopDown
  - BottomUp
- 다이나믹 프로그래밍 조건
  - 최적 부분 구조(Optional Substructure)
  - 중복되는 부분 문제(Overlapping Subproblem)
  - 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)

1. 최단 경로 알고리즘

- 단순한 다익스트라 알고리즘
- 우선순위 큐
- 개선된 다익스트라 알고리즘
- 플로이드 워셜 알고리즘

1. 기타 그래프 이론

- 서로소 집합 알고리즘
- 사이클 판별
- 위상 정렬
- 신장 트리와 크루스칼 알고리즘

1. 코딩 테스트에서 자주 출제되는 기타 알고리즘

1. 개발형 코딩 테스트
