N=int(input())
S=input()
V=[0 for i in range(26)]
c=0
V[ord(S[0])-97]+=1
c=1
for i in range(1,N):
    if S[i-1]==S[i]:
        c+=1
        V[ord(S[i])-97]=max(V[ord(S[i])-97],c)
    else:
        c=1
        V[ord(S[i])-97]=max(V[ord(S[i])-97],c)
print(sum(V))