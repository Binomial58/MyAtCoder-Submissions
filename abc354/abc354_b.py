N=int(input())
S=[]
C=0
for k in range(N):
    s,c=map(str,input().split())
    C+=int(c)
    S.append(s)
S.sort()
M=C%N
print(S[M])