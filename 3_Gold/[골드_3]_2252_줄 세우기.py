import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
height = [[] for _ in range(N+1)]
cost = [[] for _ in range(N+1)]
going_to = [0] * (N+1)

for i in range(M):
    smaller, taller = map(int,sys.stdin.readline().split())
    height[smaller].append(taller)
    going_to[taller] += 1

def topological_sort(graph):
    in_degree = []
    queue = deque()
    for i in range(1,N+1):
        if not going_to[i]:
            queue.append(i)

    while queue:
        x = queue.popleft()
        in_degree.append(x)

        for i in graph[x]:
            going_to[i] -= 1
            if going_to[i] == 0:
                queue.append(i)

    for i in in_degree:
        print(i, end=' ')

# 위상 정렬 결과 출력
topological_sort(height)