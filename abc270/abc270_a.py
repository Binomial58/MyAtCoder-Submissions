A,B=map(int, input().split())
a=[0]*3
b=[0]*3
c=[0]*3
if A>=4:
    A-=4
    a[2]=1
if A>=2:
    A-=2
    a[1]=1
if A>=1:
    A-=1
    a[0]=1
if B>=4:
    B-=4
    b[2]=1
if B>=2:
    B-=2
    b[1]=1
if B>=1:
    B-=1
    b[0]=1
for i in range(3):
    if a[i]==1 or b[i]==1:
        c[i]=1
print(c[0]+c[1]*2+c[2]*4)