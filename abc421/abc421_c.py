n=int(input())
S=input()
indexA=[]
for i in range(2*n):
    if S[i]=="A":
        indexA.append(i)
A=[2*i for i in range(n)]
B=[2*i+1 for i in range(n)]
ca=0
cb=0
for i in range(n):
    ca+=abs(indexA[i]-A[i])
    cb+=abs(indexA[i]-B[i])
print(min(ca,cb))