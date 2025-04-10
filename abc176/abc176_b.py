N=input()
S=0
for i in range(len(N)):
    S+=int(N[i])
if S%9==0:
    print("Yes")
else:
    print("No")