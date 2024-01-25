import sys

N, M = map(int, sys.stdin.readline().split())

dfs_list = []
dfs_visited = [[] for _ in range(N+1)]
cnt = 0

for i in range(N):
    dfs_list.append(list(map(str, sys.stdin.readline().strip())))

for i in range(N):
    for j in range(M):
        dfs_visited[i].append(False)

def dfs(x,y,visited):
    global cnt
    
    print(visited[x][y],x,y)
    visited[x][y] = True
    
    if x>N or y>N:
        return cnt
    
    if dfs_list[x][y] == '-':
        cnt += 1
        dfs(x,y+1,visited)
    
    if dfs_list[x][y] == '|':
        cnt += 1
        dfs(x+1,y,visited)
    
    return cnt

for i in range(N):
    for j in range(M):
        if dfs_visited[i][j] == False:
            dfs(i,j,dfs_visited)
    

print(cnt)