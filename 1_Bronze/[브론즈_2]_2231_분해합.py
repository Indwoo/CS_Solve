N = int(input())

for i in range(1, N+1):
    sum_list = sum((map(int, str(i))))
    sum_list = i + sum_list
    if sum_list == N:
        print(i)
        break
    if i == N:
        print(0)