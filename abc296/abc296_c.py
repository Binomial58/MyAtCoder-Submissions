N,X=map(int, input().split())
A=set(map(int, input().split()))
for k in A:
    if k+X in A:
        print("Yes")
        exit()
print("No")