import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

time = [0] * MAX

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == K:
            return time[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not time[next_v]:
                time[next_v] = time[v] + 1
                q.append(next_v)

N, K = map(int, input().split())
print(bfs(N))