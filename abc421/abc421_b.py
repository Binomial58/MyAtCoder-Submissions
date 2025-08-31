def rev(n):
    n=str(n)
    return int(n[::-1])
x,y=map(int, input().split())
A=[x,y]
for i in range(2,10):
    A.append(rev(A[i-2]+A[i-1]))
print(A[9])