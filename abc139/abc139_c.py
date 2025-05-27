N=int(input())
H=list(map(int, input().split()))
D=[]
E=[]
S=0
for i in range(N-1):
    if H[i]>=H[i+1]:
        D.append(1)
    else:
        D.append(0)
for i in range(N-1):
    if D[i]==1:
       S+=1
    else:
        E.append(S)
        for i in range(S):
            E.append(0)
        S=0
E.append(S) 
S=0
print(max(E))