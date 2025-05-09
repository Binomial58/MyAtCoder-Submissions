H,W=map(int, input().split())
A=[]
for _ in range(H):
    a=list(map(int, input().split()))
    A.append(a)
for i in range(W-1):
    for j in range(H-1):
        if A[j][i]+A[j+1][i+1]>A[j+1][i]+A[j][i+1]:
            print("No")
            exit()
print("Yes")