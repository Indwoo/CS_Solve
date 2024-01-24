import sys
from collections import deque

N = int(sys.stdin.readline().strip())

matrix = []

for i in range(N):
    matrix[0].append(0)
    matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    matrix[-1].append(0)

print(matrix)