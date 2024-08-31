num= []
for m in range (7):
    num.append(int(input()))

odd= []
for j in range (7):
    if num[j]%2 !=0:
        odd.append(num[j])

if len(odd) ==0:
    print ("-1")

else:
    print(sum(odd))
    print(min(odd))