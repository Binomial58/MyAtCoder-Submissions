X,Y=map(int, input().split())
Z=X
if X%Y==0:
    print(-1)
else:
    while True:
        if Y%X!=0:
            print(X)
            break
        else:
            X+=Z