x = []
under_sosu = []

n = int(input())

for i in range(n):
    x.append(int(input()))
    
for i in x:
    for z in range(2, i):
        if i % z == 0:
            continue
        else:
            under_sosu.append(z)
        print(under_sosu)