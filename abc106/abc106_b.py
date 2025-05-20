def divcount(n):
    i=0
    for j in range(1,n+1):
        if n%j==0:
            i+=1
    return i
N=int(input())
C=0
for i in range(1,N+1,2):
    if divcount(i)==8:
        C+=1
print(C)