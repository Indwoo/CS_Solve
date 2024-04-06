N = int(input())
for i in range(0, N+1):
    for j in range(i):
        print('', end=' ')
    for j in range(N-i):
        print('*', end='')
    print()