N=int(input())
A=list(map(int, input().split()))
A.sort()
for i in range(N):
    if A[i]!=i+1:
        print("No")
        exit()
print("Yes")