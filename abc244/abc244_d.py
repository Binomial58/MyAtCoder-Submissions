S=list(map(str, input().split()))
T=list(map(str, input().split()))
C=0
for i in range(3):
    if S[i]!=T[i]:
        C+=1
if C==0 or C==3:
    print("Yes")
else:
    print("No")