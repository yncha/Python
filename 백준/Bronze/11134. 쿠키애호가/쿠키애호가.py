n= int(input())
for i in range (n):
    a,b= map(int, input().split())

    if a%b !=0:
        print(a//b +1)
    else:
        print(a//b)