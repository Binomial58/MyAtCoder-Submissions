N=int(input())
M=set()
for i in range(N):
    L=list(map(str, input().split()))
    L=L[1:]
    M.add(":".join(L))
print(len(M))