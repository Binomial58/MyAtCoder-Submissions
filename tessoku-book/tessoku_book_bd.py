n,q=map(int, input().split())
s=input()
R=[]
H1=[0]
B1=[1]
for i in range(n):
    B1.append((B1[i]*100)%10007)
for i in range(n):
    H1.append((H1[i]*100+ord(s[i])-96)%10007)
H2=[0]
B2=[1]
for i in range(n):
    B2.append((B2[i]*100)%99989)
for i in range(n):
    H2.append((H2[i]*100+ord(s[i])-96)%99989)
for i in range(q):
    a,b,c,d=map(int, input().split())
    ha1=(H1[b]-B1[b-a+1]*H1[a-1])%10007
    hb1=(H1[d]-B1[d-c+1]*H1[c-1])%10007
    ha2=(H2[b]-B2[b-a+1]*H2[a-1])%99989
    hb2=(H2[d]-B2[d-c+1]*H2[c-1])%99989
    if ha1==hb1 and ha2==hb2:
        R.append("Yes")
    else:
        R.append("No")
for r in R:
    print(r)