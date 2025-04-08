N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
for i in range(M):
    if B[i] in A:
        A[A.index(B[i])]=-1
    else:
        print("No")
        exit()
print("Yes")