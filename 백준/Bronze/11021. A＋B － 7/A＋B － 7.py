T=int(input())
N=1
while N<T+1:
    A, B= map(int, input().split())
    print("Case " + "#" + str(N) +": "+ str(A+B))
    N=N+1