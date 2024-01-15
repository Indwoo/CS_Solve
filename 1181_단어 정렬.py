import sys

N = int(sys.stdin.readline())

str_list = [str(input()) for i in range(N)]

str_list = list(set(str_list))
str_list.sort(key=len)

for i in str_list:
    print(i)