n=int(input())
A=list(map(int, input().split()))
for a in range(n):
    for b in range(n):
        if a==b:
            break
        for c in range(n):
            if a==c or b==c:
                break
            if A[a]+A[b]+A[c]==1000:
                print("Yes")
                exit()
print("No")