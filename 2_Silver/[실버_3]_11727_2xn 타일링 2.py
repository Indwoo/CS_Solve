import sys

N = int(sys.stdin.readline())
tile = [0] * 1001

tile[1] = 1
tile[2] = 3

for i in range(3, N+1):
    if i % 2 == 0:
        tile[i] = (tile[i-1] * 2 + 1) % 10007
    else:
        tile[i] = (tile[i-1] * 2 - 1) % 10007

print(tile[N])
