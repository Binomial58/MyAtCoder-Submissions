x=int(input())
M=0
for b in range(1,32):
    for p in range(2,11):
        if b**p>x:
            break
        M=max(M,b**p)
print(M)