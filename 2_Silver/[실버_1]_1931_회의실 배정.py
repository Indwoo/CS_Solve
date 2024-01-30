import sys

cnt = 0
arr=[]

N = int(sys.stdin.readline())
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key = lambda x:(x[1],x[0]))
arr.append([0,0])

end = 0

for i in arr:
    if end <= i[0]:
        end = i[1]
        cnt+=1

print(cnt)
    