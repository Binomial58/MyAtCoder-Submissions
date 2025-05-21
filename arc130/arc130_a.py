N=int(input())
S=input()
T=""
C=0
c=1
for i in range(N):
    if S[i]==T:
        c+=1
    else:
        C+=c*(c-1)//2
        T=S[i]
        c=1
C+=c*(c-1)//2
print(C)