import sys

T = int(input())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        print('%d%02d'%(H, N / H))
    else:
        print('%d%02d'%(N % H, N / H + 1))
