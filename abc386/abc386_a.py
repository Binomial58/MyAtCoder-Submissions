X=list(map(int, input().split()))
Y=set(X)
a=0
b=0
if len(Y)!=2:
    print("No")
for k in X:
    if k !=a and a==0:
        a=k
    elif k!=a and k!=b and a!=0 and b==0:
        b=k
if (X.count(a)==2 and X.count(b)==2) or (X.count(a)==1 and X.count(b)==3) or (X.count(a)==3 and X.count(b)==1):
    print("Yes")