N=int(input())
S=N
for i in range(N,1,-1):
    if S%i!=0:
        S*=i
if N==30:
    S//=N
S+=1
print(S)