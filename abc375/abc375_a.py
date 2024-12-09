N=int(input())
S=input()
T=0
for i in range(N-2):
    if S[i]=="#" and S[i+1]=="." and S[i+2]=="#":
        T+=1
print(T)