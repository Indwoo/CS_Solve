import sys

sys.setrecursionlimit(10 ** 9)

cnt = 0

# N : 정점 개수 / M : 간선 개수
N, M = map(int, sys.stdin.readline().split())
dfs_list = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1,M+1):
    edge_1, edge_2 = map(int, sys.stdin.readline().split())
    dfs_list[edge_1].append(edge_2)
    dfs_list[edge_2].append(edge_1)

for i in range(1, N+1):
    if not dfs_visited[i]:
        cnt += 1
        dfs(dfs_list, i, dfs_visited)

print(cnt)
