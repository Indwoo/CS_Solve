from collections import deque

N, M, V = map(int, input().split())
dfs_list = [[] for _ in range(N+1)]
bfs_list = [[] for _ in range(N+1)]

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)


def dfs(graph, v, visited):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not dfs_visited[i]:
            dfs(graph, i, dfs_visited)


def bfs(graph, v, visited):
    queue = deque([v])
    bfs_visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(bfs_list[v]):
            if not bfs_visited[i]:
                queue.append(i)
                visited[i] = True
                

for i in range(M):
    edge_1, edge_2 = map(int, input().split())
    dfs_list[edge_1].append(edge_2)
    dfs_list[edge_2].append(edge_1)
    bfs_list[edge_1].append(edge_2)
    bfs_list[edge_2].append(edge_1)

dfs(dfs_list, V, dfs_visited)
dfs_list = [[] for _ in range(N+1)]
print("")
visited = [False] * (N+1)
bfs(bfs_list, V, bfs_visited)