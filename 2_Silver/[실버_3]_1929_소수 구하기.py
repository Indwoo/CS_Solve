M, N = map(int,input().split())   
ch = [0] * (N+1)
sosu = []
for i in range(2, N+1):
    if ch [i] == 0:
        sosu.append(i)
        for j in range(i, N+1, i):
            ch[j] = 1

for i in sosu:
    if i>=M:
        print(i)