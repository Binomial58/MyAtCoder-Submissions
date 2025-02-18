N,T=map(int, input().split())
S=input()
X=list(map(int, input().split()))
R=[]
L=[]
for i in range(N):
    if S[i]=="0":
        L.append(X[i])
    else:
        R.append(X[i])
count=0
R.sort()
L.sort()
l=0
r=0
for ant in R:
    #左端を決定
    while l<len(L) and L[l] <ant:
        l+=1
    #右端を決定
    while r<len(L) and L[r]-ant<=2*T:
        r+=1
    count+=r-l
print(count)