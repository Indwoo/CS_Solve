import sys

arr = []

K = int(sys.stdin.readline())
newbie=[]
cnt=0

for j in range(K):
    arr.append(list((map(int, sys.stdin.readline().split()))))
        
arr.sort(key = lambda x:(x[1],x[0]))
print(arr)

for i in range(K):#0,1,2,3,4
    for j in range(i+1,K):#
        if arr[i][0] < arr[j][0]:
            cnt+=1
    newbie.append(cnt)
    cnt=0

print(newbie)