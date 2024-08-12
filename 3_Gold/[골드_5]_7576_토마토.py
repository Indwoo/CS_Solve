import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, K = map(int, input().split())

tomato = []
queue = deque([])
cnt = 0

tomato = [list(map(int, input().split())) for _ in range(K)]

for i in range(K):
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < K and 0 <= ny < N and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt-1)
        
