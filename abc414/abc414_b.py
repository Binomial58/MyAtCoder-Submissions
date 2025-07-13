n=int(input())
s=""
a=0
C=[]
L=[]
for i in range(n):
    c,l=map(str, input().split())
    C.append(c)
    L.append(int(l))
for i in range(n):
    if L[i]>100:
        print("Too Long")
        exit()
    s+=C[i]*L[i]
    a+=L[i]
if a>100:
    print("Too Long")
else:
    print(s)