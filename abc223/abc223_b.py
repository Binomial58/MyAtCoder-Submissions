S=input()
A=[]
for i in range(len(S)):
    s=""
    for j in range(len(S)):
        s+=S[(i+j)%(len(S))]
    A.append(s)
A.sort()
print(A[0])
print(A[-1])