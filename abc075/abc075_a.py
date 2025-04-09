L=list(map(int, input().split()))
L.sort()
if L[1]==L[0]:
    print(L[2])
else:
    print(L[0])