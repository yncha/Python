n= int(input())
while True:
    op= input()
    if op == "=":
        break
    n2= int(input())
    if op == "+":
        n+=n2
    elif op == "-":
        n-=n2
    elif op == "*":
        n=n*n2
    elif op == "/":
        n= n//n2

print(n)