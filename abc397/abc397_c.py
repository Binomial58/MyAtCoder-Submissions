N=int(input())
A=list(map(int, input().split()))
B=[]
D=[]
c=0
M=0
C=set()
for a in A:
   if a not in C:
      C.add(a)
      c+=1
   B.append(c)
A=A[::-1]
c=0
C=set()
for a in A:
   if a not in C:
      C.add(a)
      c+=1
   D.append(c)
D=D[::-1]
for i in range(N-1):
   M=max(M,B[i]+D[i+1])
print(M)