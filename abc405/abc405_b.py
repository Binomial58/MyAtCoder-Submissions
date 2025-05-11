N,M=map(int, input().split())
A=list(map(int, input().split()))
C=0
if len(set(A))!=M:
    print(0)
    exit()
else:
    while len(set(A))==M:
        A=A[:N-1-C]
        C+=1
print(C)