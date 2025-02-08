A=list(map(int, input().split()))
c=0
B=[]
for i in range(len(A)):
    if A[i]!=i+1:
        c+=1
        B.append(i+1)
if c==2 and B[1]-B[0]==1:
    print("Yes")
else:
    print("No")
