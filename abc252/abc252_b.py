N,K=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
M=max(A)
for i in range(N):
    if A[i]!=M:
        continue
    if i+1 in B:
        print("Yes")
        exit()
print("No")