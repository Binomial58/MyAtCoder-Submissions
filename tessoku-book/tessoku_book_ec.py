n,q=map(int, input().split())
s=input()
R=[]
# 素数10007
p1=10007
H1=[0]
B1=[1]
for i in range(n):
    B1.append((B1[i]*100)%p1)
for i in range(n):
    H1.append((H1[i]*100+ord(s[i])-96)%p1)
Hr1=[0]
Br1=[1]
t=s[::-1]
for i in range(n):
    Br1.append((Br1[i]*100)%p1)
for i in range(n):
    Hr1.append((Hr1[i]*100+ord(t[i])-96)%p1)

# 素数99989
p2=99989
H2=[0]
B2=[1]
for i in range(n):
    B2.append((B2[i]*100)%p2)
for i in range(n):
    H2.append((H2[i]*100+ord(s[i])-96)%p2)
Hr2=[0]
Br2=[1]
for i in range(n):
    Br2.append((Br2[i]*100)%p2)
for i in range(n):
    Hr2.append((Hr2[i]*100+ord(t[i])-96)%p2)

for i in range(q):
    l,r=map(int, input().split())
    if (r-l)%2==0:
        # 奇数長の場合
        a=l
        b=(l+r)//2-1
        c=n-((l+r)//2+1)+1
        d=n-r+1
        ha1=(H1[b]-B1[b-a+1]*H1[a-1])%p1
        hb1=(Hr1[c]-Br1[c-d+1]*Hr1[d-1])%p1
        ha2=(H2[b]-B2[b-a+1]*H2[a-1])%p2
        hb2=(Hr2[c]-Br2[c-d+1]*Hr2[d-1])%p2
        if ha1==hb1 and ha2==hb2:
            R.append("Yes")
        else:
            R.append("No")
    else:
        # 偶数長の場合
        a=l
        b=(l+r)//2
        c=n-((l+r)//2+1)+1
        d=n-r+1
        ha1=(H1[b]-B1[b-a+1]*H1[a-1])%p1
        hb1=(Hr1[c]-Br1[c-d+1]*Hr1[d-1])%p1
        ha2=(H2[b]-B2[b-a+1]*H2[a-1])%p2
        hb2=(Hr2[c]-Br2[c-d+1]*Hr2[d-1])%p2
        if ha1==hb1 and ha2==hb2:
            R.append("Yes")
        else:
            R.append("No")
for r in R:
    print(r)
