A, B = map(int, input().split())
num_cnt = {}
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

for i in A_list:
    num_cnt[i] = i

for i in B_list:
    if i in num_cnt:
        del num_cnt[i]
    else:
        num_cnt[i] = i

print(len(num_cnt))