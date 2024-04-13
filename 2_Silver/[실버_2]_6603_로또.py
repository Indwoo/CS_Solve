from itertools import combinations

while True:
    K = list(map(int, input().split()))
    if K == [0]:
        break
    lottery = list(combinations(K[1:], 6))
    for i in lottery:
        for j in i:
            print(j, end=' ')
        print("\n", end='')
    print("\n", end='')