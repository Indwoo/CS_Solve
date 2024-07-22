import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(apart, a, b):
    n = len(apart)
    queue = deque()
    queue.append((a, b))
    apart[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if apart[nx][ny] == 1:
                apart[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


N = int(input())

apartment = []
for i in range(N):
    apartment.append(list(map(int, input().rstrip())))

cnt = []
for i in range(N):
    for j in range(N):
        if apartment[i][j] == 1:
            cnt.append(bfs(apartment, i, j))

cnt.sort()

print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])