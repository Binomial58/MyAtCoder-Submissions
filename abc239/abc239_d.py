P=[]
R=[]
for i in range(2,201):
    j=2
    c=1
    while j*j<=i:
        if i%j==0:
            c=0
            break
        j+=1
    if c==1:
        P.append(i) 
a,b,c,d=map(int, input().split())
for t in range(a,b+1):
    r=0
    for a in range(c,d+1):
        if (t+a) in P:
            r+=1
    R.append(r)
if min(R)==0:
    print("Takahashi")
else:
    print("Aoki")