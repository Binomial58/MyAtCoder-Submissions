X=int(input())
B=[]
for a in range(1,10):
    for b in range(1,10):
        B.append(a*b)
print(2025-X*(B.count(X)))