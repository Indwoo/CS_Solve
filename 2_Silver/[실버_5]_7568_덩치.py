N = int(input())
d_list = []
list_cnt = []

cnt = 0
for i in range(N):
    d_list.append(list(map(int,input().split())))

for i in d_list:
    cnt = 1
    for j in d_list:
        if i[0] < j[0] and i[1] < j[1]:
            cnt+=1
    
    print(cnt, end=' ')
