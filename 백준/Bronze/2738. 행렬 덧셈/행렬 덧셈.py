a,b = map(int,input().split())
i=[]
for n in range(a):
    p=list(map(int,input().split()))
    i.append(p)
l=[]
for m in range(a):
    q= list(map(int,input().split()))
    l.append(q)

for x in range(a):
    for z in range(b):
        print(i[x][z]+ l[x][z], end= " ")
    print()