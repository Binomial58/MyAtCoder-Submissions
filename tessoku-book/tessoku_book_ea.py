n=int(input())
count=0
C={}
for i in range(n):
    a=int(input())
    if a in C:
        count+=C[a]
        C[a]+=1
    else:
        C[a]=1
print(count)