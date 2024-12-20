N,T=map(int, input().split())
C=list(map(int, input().split()))
R=list(map(int, input().split()))
#対応するインデックスを全て返す
if C.count(T)!=0:
    I=[i for i, x in enumerate(C) if x ==T]
    D=[r for r in (R[k] for k in I)]
    print(I[D.index(max(D))]+1)
else:
    I=[i for i, x in enumerate(C) if x==C[0]]
    D=[r for r in (R[k] for k in I)]
    print(I[D.index(max(D))]+1)