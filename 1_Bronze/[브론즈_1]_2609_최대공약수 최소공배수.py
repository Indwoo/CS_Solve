N, M = map(int, input().split())
Min_Mul = 0
if N > M:
    for i in range(M, 0, -1):
        if N % i == 0 and M % i == 0:
            Min_Mul = i
            print(i)
            break
else:
    for i in range(N, 0, -1):
        if N % i == 0 and M % i == 0:
            Min_Mul = i
            print(i)
            break
print(Min_Mul * N//Min_Mul * M//Min_Mul)
