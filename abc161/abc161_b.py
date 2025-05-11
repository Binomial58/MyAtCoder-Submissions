N,M=map(int, input().split())
A=list(map(int, input().split()))
C=0
for a in A:
   if a>=sum(A)/(4*M):
      C+=1 
if C>=M:
   print("Yes")
else:
   print("No")