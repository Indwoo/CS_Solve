import sys

A, B, C = map(int, sys.stdin.readline().split())
C -= B
if C > 0:
    print(A//C+1)
else:
    print(-1)

# for i in range(1, 10000000001):
#     if A*i < C*i:
#         print(i)
#         exit()
