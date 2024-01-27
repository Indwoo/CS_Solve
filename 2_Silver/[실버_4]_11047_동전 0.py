import sys
N, K = map(int, input().split())
cnt = 0
less = 0
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline().strip()))
    if coin[i] > K:
        less = i

while (K != 0):
    cnt += (K // coin[less-1])
    K = K - (coin[less-1] * (K // coin[less-1]))
    less = less-1

print(cnt)
