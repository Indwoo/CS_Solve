import sys

N = int(sys.stdin.readline())

a = 0
b = 1
c = 0

for _ in range(N):
    c = (a+b)%15746
    a = b
    b = c
    
if N ==1:
    print("1")
else:
    print(c)
