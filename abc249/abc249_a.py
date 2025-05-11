A,B,C,D,E,F,X=map(int, input().split())
T=0
R=0
t=0
r=0
for x in range(X):
    if t>=0:
        T+=B
    if r>=0:
        R+=E
    t+=1
    r+=1
    if t==A:
        t=-C
    if r==D:
        r=-F
if T>R:
    print("Takahashi")
elif R>T:
    print("Aoki")
else:
    print("Draw")