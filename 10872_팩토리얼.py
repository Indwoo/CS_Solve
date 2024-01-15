def ind_fact(n):
    tot=1
    if n > 0:
        tot = n * ind_fact(n-1)
    return tot

n = int(input())
print(ind_fact(n))
