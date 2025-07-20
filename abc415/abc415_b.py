S=input()
c=0
i=0
A=[]
for i in range(len(S)):
    if S[i]=="#":
        A.append(i+1)
for i in range(len(A)//2):
    print(str(A[2*i])+","+str(A[2*i+1]))