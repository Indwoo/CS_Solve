i, j, k = map(int, input().split())

if i == j == k:
    print(10000+i*1000)
elif i == j:
    print(1000+i*100)
elif i == k:
    print(1000+i*100)
elif j == k:
    print(1000+j*100)
else:
    print(100 + max(i,j,k))