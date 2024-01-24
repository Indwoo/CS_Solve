import sys
from collections import deque

N, M, K, X = map(int, input().split())
city_list = [[] for _ in range(N+1)]
able_city = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    city_list[a].append(b)

def bfs(graph, start):
    global able_city
    queue = deque()
    queue.append(start)
    visited = {} 
    
    visited[start] = 0
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1  # 이웃 노드의 거리 갱신
                queue.append(neighbor)
                
    keys = [key for key, value in visited.items() if value == K]
    keys.sort()
    
    if len(keys) == 0:
        print("-1")
    else:
        for key in keys:
            print(key)

bfs(city_list, X)