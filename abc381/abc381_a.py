N=int(input())
S=input()
#/の配列番号
M=(N+1)//2-1
if N%2==0 or S[M]!="/":
    print("No")
else:
    if all([S[v]=="1" for v in range(M)])and all([S[u]=="2" for u in range(M+1,N)]):
        print("Yes")
    else:
        print("No")