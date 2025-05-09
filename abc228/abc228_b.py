N,X=map(int, input().split())
A=list(map(int, input().split()))
S=1
a=X-1
B=set([a])
for i in range(N-1):
    a=A[a]-1
    if a in B:
        print(S)
        exit()
    B.add(a)
    S+=1
print(S)