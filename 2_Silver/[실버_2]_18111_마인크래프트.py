N, M, B = map(int, input().split())
mine = []
height = 0
ans = 1000000000000

for i in range(N):
    mine.append(list(map(int, input().split())))

for i in range(257):
    max, min = 0, 0
    for j in range(N):
        for k in range(M):
            if mine[j][k] > i:
                max += mine[j][k] - i
            else:
                min += i - mine[j][k]
    inventory = max + B
    
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i
print(ans, height)
