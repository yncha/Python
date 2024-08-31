while True:
    a,b,c= map(int, input().split())
    number=[]
    number.append(a)
    number.append(b)
    number.append(c)
    number.sort()
    if a==0 and b==0 and c==0:
        break
    

    else :
        if number[0] ** 2 + number [1] ** 2 == number [2] ** 2:
            print("right")
        else :
            print("wrong")