A, B, V = map(int, input().split())
day_cnt = 0
per_day = A - B
last_day = V - B

if (last_day % per_day == 0):
    print(last_day // per_day)
else:
    print(last_day // per_day + 1)
