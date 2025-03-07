N,X=map(int, input().split())
S=list(map(int, input().split()))
for i in range(1,N,2):
    S[i]-=1
if X>=sum(S):
    print("Yes")
else:
    print("No")