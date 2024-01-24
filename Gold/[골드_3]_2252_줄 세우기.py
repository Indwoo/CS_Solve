import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
height = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    height[A].append([B])
    
def topological_sort(graph):   

    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque(node for node in in_degree if in_degree[node] == 0)

    sorted_order = []

    while queue:
        node = queue.popleft()  
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(graph):
        return False

    return sorted_order

# 위상 정렬 결과 출력
print(topological_sort(height))