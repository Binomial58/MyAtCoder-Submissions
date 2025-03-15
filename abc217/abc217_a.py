L=list(map(str, input().split()))
T=L[0]
L.sort()
if T==L[0]:
    print("Yes")
else:
    print("No")