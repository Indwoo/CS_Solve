while(True):
    rec_tri = list(map(int, input().split()))
    rec_tri = sorted(rec_tri)
    if sum(rec_tri) == 0:
        break
    elif rec_tri[0]**2 + rec_tri[1]**2 == rec_tri[2]**2:
        print('right')
    else:
        print('wrong')
    
