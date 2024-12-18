N,M=map(int, input().split())
S=input()
S+="0"
max1=0
maxr=0
m=0
e=0
r=0
#必要なシャツの数とロゴの数を計算
for n in range(N+1):
    if S[n]!="0":
        m+=1
        if S[n]=="2":
            r+=1
    else:
        if m>max1:
            max1=m
            maxr=max(maxr,r)
        m=0
        r=0
maxw=max1-maxr
mlogo=maxw-M

max2=0
k=0
#必要なロゴ入りのシャツの計算
for n in range(N):
    if S[n]!="0":
        if S[n]=="2":
            k+=1
    else:
        max2=max(max2,k)
        k=0
max2=max(max2,k)
t=mlogo+maxr
print(max(max2,t))