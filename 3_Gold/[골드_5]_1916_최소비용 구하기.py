import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(graph, start):
    distance = [int(1e9)] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            distances = dist + next_dist
            if distances < distance[next_node]:
                distance[next_node] = distances
                heapq.heappush(queue, [distances, next_node])
    
    return distance

dist_start = dijkstra(graph, start)
print(dist_start[end])