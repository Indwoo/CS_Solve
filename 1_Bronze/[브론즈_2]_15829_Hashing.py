L = int(input())

hash_str = list(map(ord, input()))
hash_str = [ i-96 for i in hash_str]

cnt = 0
for i in range(len(hash_str)):
    cnt += hash_str[i] * (31**i)

print(cnt%1234567891)