#8進数に変換する関数
def eight(N):
    C=""
    while N!=0:
        C+=str(N%8)
        N//=8
    D=""
    for i in range(len(C)):
        D+=C[len(C)-i-1]
    return D
N=int(input())
S=0
for i in range(1,N+1):
    if "7" not in eight(i) and "7" not in str(i):
        S+=1
print(S)