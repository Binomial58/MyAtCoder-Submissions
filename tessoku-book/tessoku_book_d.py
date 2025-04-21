#2進数に変換する関数
def bin(N):
    C=""
    while N!=0:
        C+=str(N%2)
        N//=2
    D=""
    for i in range(len(C)):
        D+=C[len(C)-i-1]
    D="0"*(10-len(D))+D
    return D
N=int(input())
print(bin(N))