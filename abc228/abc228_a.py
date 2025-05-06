S,T,X=map(int, input().split())
if S==X:
        print("Yes")
        exit()
if S<=T:
     N=T-S
else:
     N=24-S+T
for i in range(N):
    if S==24:
        S=0
    if S==X:
        print("Yes")
        exit()
    S+=1
print("No")