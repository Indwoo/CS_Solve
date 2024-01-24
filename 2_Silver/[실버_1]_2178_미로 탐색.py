from collections import deque
import sys

N, M = map(int, input().split())
bfs_list = []

for i in range(N):
    bfs_list.append(list(map(int, sys.stdin.readline().strip())))
     
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue= deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if bfs_list[nx][ny] == 0:
                continue
            if bfs_list[nx][ny] == 1:
                bfs_list[nx][ny] = bfs_list[x][y] + 1
                queue.append((nx, ny))
                
    return bfs_list[N-1][M-1]

print(bfs(0,0))