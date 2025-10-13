def sumD(n):
    s=str(n)
    c=0
    for i in s:
        c+=int(i)
    return c
n=int(input())
A=[sumD(1)]
for i in range(n-1):
    a=sum(A)
    A.append(sumD(a))
print(sum(A))