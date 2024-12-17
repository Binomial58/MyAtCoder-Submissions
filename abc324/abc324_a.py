N=int(input())
A=list(map(int, input().split()))
for i in range(1,N):
    if A[i]!=A[0]:
        print("No")
        exit()
print("Yes")