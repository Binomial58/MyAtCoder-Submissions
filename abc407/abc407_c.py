def Security(N):
    C=0
    T=int(N[-1])
    for i in range(len(N)-1):
        C+=T
        D=(int(N[len(N)-i-2])-C)%10
        T=D
    C+=(int(N[0])-C)%10
    return C    
S=input()
L=len(S)
print(Security(S)+L)