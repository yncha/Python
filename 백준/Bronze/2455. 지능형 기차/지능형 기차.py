people=[]
a1,b1= map(int,input().split())
a2,b2= map(int,input().split())
a3,b3= map(int,input().split())
a4,b4= map(int,input().split())

people.append(b1)
people.append(b1-a2+b2)
people.append(b1-a2+b2-a3+b3)
people.append(b1-a2+b2-a3+b3-a4+b4)

print(max(people))