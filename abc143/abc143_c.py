N=int(input())
S=input()
s=S[0]
C=1
for i in range(1,N):
    if s!=S[i]:
        C+=1
        s=S[i]
print(C)