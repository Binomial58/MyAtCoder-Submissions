S=input()
X=""
Y=""
x=0
y=0
for i in range(len(S)):
    if i%2==0:
        X+="0"
        Y+="1"
    else:
        X+="1"
        Y+="0"
for j in range(len(S)):
    if S[j]!=X[j]:
        x+=1
    if S[j]!=Y[j]:
        y+=1
print(min(x,y))