cnt = 0
is_sosu = True

N = int(input())
j = list(map(int, input().split()))

for i in range(N):
    if j[i]==1:
        continue
    for x in range(2, j[i]):
        if j[i] % x == 0:
            is_sosu = False
            break
    if is_sosu == True:
        cnt += 1
    else:
        is_sosu = True
print(cnt)
