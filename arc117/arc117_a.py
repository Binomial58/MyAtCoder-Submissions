A,B=map(int, input().split())
a=[]
b=[]
if A==B:
    for i in range(1,A+1):
        a.append(i)
        b.append(-i)
elif  A>B:
    for i in range(1,A-B+2):
        a.append(i)
    b.append(-sum(a))
    for j in range(B-1):
        a.append(10**4-j)
        b.append(-(10**4-j))
else:
    for i in range(1,B-A+2):
        b.append(-i)
    a.append(-sum(b))
    for j in range(A-1):
        a.append(10**4-j)
        b.append(-(10**4-j))
print(*(a+b))