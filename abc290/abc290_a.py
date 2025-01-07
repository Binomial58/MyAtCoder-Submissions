N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
S=0
for i in B:
    S+=A[i-1]
print(S)