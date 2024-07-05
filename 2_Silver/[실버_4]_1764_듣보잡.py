import sys

N, M = map(int, sys.stdin.readline().split())
A = set([])
B = set([])

for _ in range(N):
    A.add(sys.stdin.readline().strip())
    
for _ in range(M):
    B.add(sys.stdin.readline().strip())

C = A.intersection(B)

print(len(C))
for i in sorted(C):
    print(i)