n,m=map(int, input().split())
A=list(map(int, input().split()))
for i in range(n):
    if m==sum(A)-A[i]:
        print("Yes")
        exit()
print("No")