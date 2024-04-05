X = list(map(str, input()))
answer = 0

if X[1] == 'x':
    X = list(reversed(X))
    for i in range(len(X)-2):
        if X[i] == 'a' :
            answer += 16**i * 10
        elif X[i] == 'b' :
            answer += 16**i * 11
        elif X[i] == 'c' :
            answer += 16**i * 12
        elif X[i] == 'd' :
            answer += 16**i * 13
        elif X[i] == 'e' :
            answer += 16**i * 14
        elif X[i] == 'f' :
            answer += 16**i * 15
        else:
            answer += 16**i * int(X[i])
    print(answer)
elif X[0] == '0':
    X = list(reversed(X))
    for i in range(len(X)-1):
        answer += 8**i * int(X[i])
    print(answer)
else:
    for i in range(len(X)):
        print(X[i], end='')