S=[]
C=0
for i in range(3):
    a,b=map(int, input().split())
    S.append(a)
    S.append(b)
for i in range(1,5):
    if S.count(i)==2:
        C+=1
if C==2:
    print("YES")
else:
    print("NO")