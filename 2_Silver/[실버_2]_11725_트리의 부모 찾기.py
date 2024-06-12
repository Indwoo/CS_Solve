import sys
from collections import deque

N = int(sys.stdin.readline())
is_linked = [[0] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    is_linked[a].append(b)
    is_linked[b].append(a)
    
parent[1] = 0
q = deque()
q.append(1)

while q:
    current = q.popleft()
    for v in is_linked[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)

for p in parent[2:]:
	print(p)