n=int(input())
d=2025-n
A=[]
B=[]
for i in range(1,10):
    if d%i==0 and 1<=d//i<=9:
        A.append(i)
        B.append(d//i)
for i in range(len(A)):
    print(A[i],"x",B[i])