import sys
import heapq

V, E = list(map(int, sys.stdin.readline().split()))
cost = [[] for _ in range(V+1)]

for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    cost[A].append([C, B])
    cost[B].append([C, A])

visited = [False] * (V+1)
answer = 0
cnt = 0

heap = []
heapq.heappush(heap, (0, 1))

while cnt < V:
    C, A = heapq.heappop(heap)
    print(heap)
    if visited[A]:
        continue
    visited[A] = True
    answer += C
    cnt += 1
    for i in cost[A]:
        heapq.heappush(heap, i)

print(answer)