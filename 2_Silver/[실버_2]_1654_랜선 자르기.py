import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LAN = []
cnt = 0

for i in range(K):
    LAN.append(int(input()))

left = 1
right = max(LAN)

while left<=right:
    mid = (left+right) // 2
    cnt = 0
    for x in LAN:
        cnt += x//mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)    
    
