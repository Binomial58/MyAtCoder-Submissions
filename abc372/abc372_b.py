M=int(input())
a=M
#B:余り
B=[]
C=[]
while a>=3:
    a=M//3
    b=M%3
    B.append(b)
    M=a
B.append(a)
for v in range(len(B)):
    for u in range(B[v]):
        C.append(v)
print(len(C))
print(*C)