A=int(input())
B=int(input())
C=int(input())
X=int(input())
r=0

for i in range(A+1):
    if(500*i>X):
        break
    Y=X-500*i
    for j in range(B+1):
        if(100*j>Y):
            break
        Z=Y-100*j
        for k in range(C+1):
            if(50*k>Z):
                break
            W=Z-50*k
            if(W==0):
                r+=1
print(r)