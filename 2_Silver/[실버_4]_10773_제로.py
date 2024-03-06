sum_list=[]
K = int(input())

for i in range(K):
    N = int(input())
    if N == 0:
        sum_list.pop()
    else:
        sum_list.append(N)
            
print(sum(sum_list))