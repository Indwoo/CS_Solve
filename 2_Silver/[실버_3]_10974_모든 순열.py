from itertools import permutations

N = int(input())
all_list = [i for i in range(1, N+1)]
per_list = list(permutations(all_list, N))
per_list = sorted(per_list)

for i in per_list:
    for j in i:
        print(j, end = ' ')
    print("\n", end = '')