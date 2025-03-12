N,X,T=map(int, input().split())
if N%X==0:
    S=N//X
else:
    S=N//X+1
print(S*T)