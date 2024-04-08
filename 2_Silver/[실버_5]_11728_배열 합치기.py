N, M = map(int, input().split())
num_cnt = []
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

for i in A_list:
    num_cnt.append(i)
    
for i in B_list:
    num_cnt.append(i)

num_cnt = sorted(num_cnt)
print(' '.join(map(str, num_cnt)))