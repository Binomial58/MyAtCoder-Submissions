S=input()
T=input()
A=[]
B=[]
a=S[0]
d=1
for i in range(1,len(S)):
    if S[i]==a:
        d+=1
    else:
        A.append([a,d])
        a=S[i]
        d=1
A.append([a,d])
a=T[0]
d=1
for i in range(1,len(T)):
    if T[i]==a:
        d+=1
    else:
        B.append([a,d])
        a=T[i]
        d=1
B.append([a,d])
if len(A)!=len(B):
    print("No")
    exit()
else:
    for i in range(len(A)):
        if A[i][0]!=B[i][0]:
            print("No")
            exit()
        if A[i][1]!=B[i][1]:
            if A[i][1]==1 or A[i][1]>B[i][1]:
                print("No")
                exit()
print("Yes")