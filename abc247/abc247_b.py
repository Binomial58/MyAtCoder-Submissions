N=int(input())
S,T=[],[]
for i in range(N):
    s,t=map(str, input().split())
    S.append(s)
    T.append(t)
A,B=[],[]
for i in range(N):
    A.append(S.count(S[i])+T.count(S[i]))
    B.append(T.count(T[i])+S.count(T[i]))
    if S[i]==T[i]:
        A[i]=1
        B[i]=1
for i in range(N):
    if A[i]!=1 and B[i]!=1:
        print("No")
        exit()
print("Yes")