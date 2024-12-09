A,B,C=map(int,input().split())
D=[]
if B>C:
    E=24-B+C
else:
    E=C-B
d=B
for i in range(E+1):
    if d==24:
        d=0
    D.append(d) 
    d+=1
if D.count(A)==1:
    print("No")
else:
    print("Yes")