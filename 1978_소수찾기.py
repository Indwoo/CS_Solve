cnt = 0
N = int(input())
j = list(map(int, input().split()))
print(j)
for i in j:
    print(i)
    for x in range(2, 1001):
        if i % x == 0:
            print(f'{i}는 {x}로 나눠짐!')
            break
        else:
            print(f'{i}는 소수!')
            cnt += 1
            break
print(cnt)
