def rounding(x,k):
    S=str(x)
    d=len(S)-k-1
    if int(S[d])>=5:
        return str(int(S[:d])+1)+"0"*(len(S[d:]))
    else:
        return str(int(S[:d]))+"0"*(len(S[d:]))
X,K=map(int, input().split())
if len(str(X))>K:
    for i in range(K):
        X=int(rounding(X,i))
else:
    if len(str(X))==K:
        for i in range(K-1):
            X=int(rounding(X,i))
        if K!=len(str(X)):
            X=int(rounding(X,K-1))
        else:
            if int(str(X)[0])<5:
                X=0
            else:
                X=10**(len((str(X))))
    else:
        for i in range(len(str(X))-1):
            X=int(rounding(X,i))
        if int(str(X)[0])<5:
            X=0
        else:
            X=10**(len((str(X))))
        if int(str(X)[0])<5:
            X=0
        else:
            X=10**(len((str(X))))
print(X)
