a, b, c= map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b!=c or a==c!=b:
    print(1000+a*100)
elif b==c!=a:
    print(1000+b*100)
elif a!=b!=c:
    print(max(a,b,c)*100)