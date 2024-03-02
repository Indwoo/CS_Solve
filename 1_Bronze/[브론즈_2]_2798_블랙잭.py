import itertools

N, M = map(int, input().split())

answer = 0
last_num = 0

card_list = list(map(int,input().split()))

card_3_sum = list(itertools.combinations(card_list,3))

for i in range(len(card_3_sum)):
    now_sum = sum(card_3_sum[i])
    if M < now_sum:
        continue
    if M - last_num > M - now_sum:
        answer = now_sum
        last_num = now_sum
    
print(answer)
