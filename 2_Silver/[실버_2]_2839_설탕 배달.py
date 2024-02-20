N = int(input())
tot = 0

if N % 5 == 0:
    print(N//5)

else:
    while N >= 0:
        N -= 3
        tot += 1
        if N % 5 == 0:
            tot += N // 5
            print(tot)
            break
        elif N == 1 or N == 2:
            print("-1")
            break
        elif N == 0:
            print(tot)
            break
