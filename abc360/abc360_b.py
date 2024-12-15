S,T=map(str,input().split())
L=len(S)
A=""
for w in range(1,L):
    for c in range(1,w+1):
        A=""
        for k in range(c-1,L,w):
            B=S[k]
            #文字列の結合
            A+=B
        if A==T:
            print("Yes")
            exit()
else:
    print("No")