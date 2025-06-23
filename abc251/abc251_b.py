N,W=map(int, input().split())
A=list(map(int, input().split()))
A+=[0,0]
K=set()
for a in range(N+2):
    for b in range(N+2):
        if a==b:
            break
        for c in range(N+2):
            if a==c or b==c:
                break
            if A[a]+A[b]+A[c]<=W:
                K.add(A[a]+A[b]+A[c])
print(len(K))