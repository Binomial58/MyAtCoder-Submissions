def bin(N):
    C=""
    while N!=0:
        C+=str(N%2)
        N//=2
    D=""
    for i in range(len(C)):
        D+=C[len(C)-i-1]
    return int(D)
K=int(input())
print(bin(K)*2)