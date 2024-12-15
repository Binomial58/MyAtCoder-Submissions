A=[]
M=1
while M!=0:
    M=int(input())
    A.append(M)
L=len(A)
for k in range(L-1,-1,-1):
    print(A[k])