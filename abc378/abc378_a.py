A=list(map(int,input().split()))
A.append(5)
A.sort(reverse=True)
S=0
for i in range(4):
    if A[i]==A[i+1]:
        S+=1
        A[i]=0
        A[i+1]=0
print(S)