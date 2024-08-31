a,b = map(int,input().split())
basket=[]
for i in range(a):
    basket.append(0)
for l in range(b):
    z,y,x= map(int, input().split())
    for n in range(z-1, y):
        basket[n]=x
print(*basket)