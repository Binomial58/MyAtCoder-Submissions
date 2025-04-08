def bin(N):
    C=""
    while N!=0:
        C+=str(N%2)
        N//=2
    D=""
    for i in range(len(C)):
        D+=C[len(C)-i-1]
    return D
def dec(T):
    S=0
    for i in range(len(T)):
        S+=int(E[i])*(2**(len(T)-i-1))
    return S
A,B=map(int, input().split())
A=bin(A)
B=bin(B)
if len(A)<len(B):
    A="0"*(len(B)-len(A))+A
else:
    B="0"*(len(A)-len(B))+B
E=""
for k in range(len(A)):
    if (B[k]=="1" and A[k]=="1") or (B[k]=="0" and A[k]=="0"):
        E+="0"
    else:
        E+="1"
print(dec(E))