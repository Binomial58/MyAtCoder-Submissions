N=int(input())
F=0
for i in range(len(str(N))):
    F+=int(str(N)[i])
if N%F==0:
    print("Yes")
else:
    print("No")