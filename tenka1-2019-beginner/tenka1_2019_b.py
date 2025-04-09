N=int(input())
S=input()
K=int(input())
k=S[K-1]
s=""
for i in range(N):
    if S[i]!=k:
        s+="*"
    else:
        s+=S[i]
print(s)