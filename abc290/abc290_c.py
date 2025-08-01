n,k=map(int, input().split())
A=list(map(int, input().split()))
S=set(A)
for i in range(k):
    if i not in S:
        print(i)
        exit()
print(k)