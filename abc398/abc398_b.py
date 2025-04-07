A=list(map(int, input().split()))
C=[0]*(13)
for i in range(7):
    C[A[i]-1]+=1
if (C.count(5)==1)and(C.count(2)==1):
    print("Yes")
elif C.count(4)==1:
    if (C.count(3)==1) or (C.count(2)==1):
        print("Yes")
    else:
        print("No")
elif C.count(3)==2:
    print("Yes")
elif C.count(3)==1:
    if (C.count(2)==1) or (C.count(2)==2):
        print("Yes")
    else:
        print("No")
else:
    print("No")