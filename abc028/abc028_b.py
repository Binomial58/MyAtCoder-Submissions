S=input()
X=["A","B","C","D","E","F"]
R=[0 for i in range(6)]
for s in S:
    R[X.index(s)]+=1
print(*R)