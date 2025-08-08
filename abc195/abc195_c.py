n=int(input())
l=len(str(n))
c=0
for i in range(1,l):
    c+=(10**i-10**(i-1))*((i-1)//3)
c+=(n+1-10**(l-1))*((l-1)//3)
print(c)