def factorial(n):
    S=1
    for i in range(1,n+1):
        S*=i
    return S
P=int(input())
D=0
C=[factorial(n) for n in range(1,11)]
for i in range(9,-1,-1):
    D+=P//C[i]
    P%=C[i]
print(D)