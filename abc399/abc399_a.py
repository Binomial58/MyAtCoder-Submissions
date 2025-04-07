N=int(input())
S=input()
T=input()
c=0
for i in range(N):
    if S[i]==T[i]:
        c+=1
print(N-c)