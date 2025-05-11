A,B,C,D=map(int, input().split())
T=0
U=0
while A>D*U and T!=10**5:
        A+=B
        U+=C
        T+=1
if A<=U*D:
    print(T)
else:
    print(-1)