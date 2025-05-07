N=int(input())
if N==0:
    print("Yes")
    exit()
while N%10==0:
    N//=10
N=str(N)
if len(N)%2==0:
    R=len(N)//2
else:
    R=(len(N)-1)//2
if R==1:
    if N[0]==N[-1]:
        print("Yes")
    else:
        print("No")
    exit()
for i in range(R):
    if N[i]!=N[len(N)-i-1]:
        print("No")
        exit()
print("Yes")