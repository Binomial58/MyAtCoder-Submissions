L=list(map(int, input().split()))
for i in range(4):
    if L[i]==sum(L)-L[i]:
        print("Yes")
        exit()
for a in range(4):
    for b in range(4):
        if a==b:
            break
        if L[a]+L[b]==sum(L)-L[a]-L[b]:
            print("Yes")
            exit()
print("No")