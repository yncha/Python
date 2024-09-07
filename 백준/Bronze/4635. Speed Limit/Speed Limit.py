while True:
    n= int(input())
    if n==-1:
        break
    a=[]
    y1=0
    
    for i in range(n):
        x,y= map(int,input().split())
        a.append(x*(y-y1))
        y1=y
    print(sum(a), "miles")