N=int(input())
A=[]
if N==1:
    print(1)
    print(1)
    exit()
for i in range(1,N+1):
    if i %2==0:
        A.append(i)
print(len(A))
print(*A)