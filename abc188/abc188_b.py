N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
S=0
for i in range(N):
    S+=A[i]*B[i]
if S==0:
    print("Yes")
else:
    print("No")