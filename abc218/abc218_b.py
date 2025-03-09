P=list(map(int, input().split()))
L=[]
for p in P:
    L.append(chr(96+p))
print("".join(L))