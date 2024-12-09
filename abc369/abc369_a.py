A,B=map(int,input().split())
S=abs(A-B)
if S==0:
    print(1)
elif S%2==0:
    print(3)
else:
    print(2)