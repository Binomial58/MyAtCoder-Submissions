import copy
N,X=map(int,input().split())
A=list(map(int, input().split()))
M=101
for i in range(0,101):
    B=copy.deepcopy(A)
    B.append(i)
    B.sort()
    if sum(B)-B[0]-B[-1]>=X:
        M=min(i,M)
if M==101:
    M=-1
print(M)