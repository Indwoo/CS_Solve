import sys

A, B, C = map(int, sys.stdin.readline().split())
C -= B
if C > 0:
    print(A//C+1)
else:
    print(-1)