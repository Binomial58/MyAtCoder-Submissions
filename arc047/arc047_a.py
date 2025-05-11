N,L=map(int, input().split())
S=input()
A=0
B=1
for i in range(N):
    if S[i]=="+":
        B+=1
        if B==L+1:
            A+=1
            B=1
    else:
        B-=1
print(A)