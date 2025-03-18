while True :
    pwd = input()
    if pwd == "END" :
        break
    else :
        pwd = pwd[::-1]
        print(pwd)