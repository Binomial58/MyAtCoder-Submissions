n=int(input())
A=[1]
y=0
for j in range(n+1):
    if y>=2:
        A=[sum(A[1:])]+A
    else:
        A=[0]+A
    y+=1
print(sum(A))