from collections import deque
import sys

N, M = map(int, input().split())

bfs_list = [ [] for _ in range (N+2)]
visited_list = [False] * (N+2)

queue = deque(bfs_list)
print(queue)

queue.appendleft([0 for i in range (M+2)])
queue.append([0 for i in range (M+2)])
for i in range(N):
    bfs_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

print(queue)

