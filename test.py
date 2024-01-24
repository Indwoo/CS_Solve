import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix = {}

for i in range(N):
    key, val = sys.stdin.readline().split()
    if key in matrix:
        matrix[key].append(val)
    else:
        matrix[key] = [val]
    
print(matrix)