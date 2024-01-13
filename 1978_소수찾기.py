cnt = 0
is_sosu = True
N = int(input())
j = list(map(int, input().split()))
for i in range(N):
    if j[i]==1:
        continue
    for x in range(2, j[i]):
        if j[i] % x == 0:
            print(f'{j[i]}가 {x}로 나눠떨어짐!!')
            is_sosu = False
            print('is_sosu = False')
            break
    if is_sosu == True:
        print(f'{j[i]}소수니까 cnt에 1 추가')
        cnt += 1
    else:
        print('sosu 아님')
        is_sosu = True
print(cnt)