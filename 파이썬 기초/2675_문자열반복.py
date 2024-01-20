all_time = int(input())
for i in range(all_time):
    x = list(input().split())
    repeat_str = list(x[1])
    repeat_time = int(x[0])
    result = ''
    for j in range(len(repeat_str)):
        result += repeat_str[j] * repeat_time
    print(result)