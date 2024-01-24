import sys

N, M = map(int, sys.stdin.readline().split())
height = [[] for _ in range(M+1)]

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    height[A].append([A, B])
    height[B].append([B, A])
    
print(height)