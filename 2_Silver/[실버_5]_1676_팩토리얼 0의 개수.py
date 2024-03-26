def ind_fact(n):
    tot=1
    if n > 0:
        tot = n * ind_fact(n-1)
    return tot

N = int(input())
fact = ind_fact(N)
fact_list = list(map(str, str(fact)))
count = 0
for i in range(len(fact_list)-1, -1, -1):
    if fact_list[i] == '0':
        count += 1
    else:
        break
print(count)