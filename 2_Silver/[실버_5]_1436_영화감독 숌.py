N = int(input())
num_list = []
doom = 666
cnt = 0

while(1):
    if '666' in str(doom):
        cnt += 1
    if cnt == N:
        print(doom)
        break
    doom+=1