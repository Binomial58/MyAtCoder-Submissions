N=int(input())
B=set()
A=[]
for i in range(N):
    W=input()
    A.append(W)
a=A[0]
B.add(a)
for i in range(N-1):
    if A[i+1] in B:
        print("No")
        exit()
    if a[-1]!=A[i+1][0]:
        print("No")
        exit()
    a=A[i+1]
    B.add(a)
print("Yes")
