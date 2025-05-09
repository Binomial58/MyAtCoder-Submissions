N=int(input())
A=[]
while N>0:
    if N>=8:
        N-=8
        A.append(8)
    elif N>=4:
        N-=4
        A.append(4)
    elif N>=2:
        N-=2
        A.append(2)
    else:
        N-=1
        A.append(1)
print(len(A))
for a in A:
    print(a)