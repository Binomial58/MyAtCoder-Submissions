n=int(input())
A=list(map(int, input().split()))
A.sort()
m=(n-1)//2
L=A[:m]
R=A[m+1:]
B=[]
for i in range(n//2):
    B.append(L[i])
    B.append(R[i])
B.append(A[m])
for i in range(n//2):
    j=2*i+1
    if B[j-1]>=B[j] or B[j]<=B[j+1]:
        print("No")
        exit()
print("Yes")