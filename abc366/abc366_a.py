N,T,A=map(int,input().split())
d=abs(T-A)
M=N-(A+T)
if d>M:
    print("Yes")
else:
    print("No")