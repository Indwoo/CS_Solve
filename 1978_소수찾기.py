cnt = 0
N = int(input())
j = list(map(int, input().split()))
for i in j:
    print(i)
    for x in range(2, 1001):
        if i % x == 0:
            break
        else:
            continue
    cnt+=1
print(cnt)
