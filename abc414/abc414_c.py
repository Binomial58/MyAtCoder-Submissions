def N_ary(N,A):
    C = ""
    while A != 0:
        C += str(A % N)
        A //= N
    D = ""
    for i in range(len(C)):
        D += C[len(C) - i - 1]
    return D
a=int(input())
n=int(input())
s=0
l=len(str(n))
if l%2==0:
    l//=2
else:
    l=l//2+1
for i in range(10**l):
    o=str(i)
    l=len(o)
    x=int(o[:l-1]+o[::-1])
    y=int(o[:l]+o[::-1])
    x_a=N_ary(a,x)
    y_a=N_ary(a,y)
    if x_a==x_a[::-1] and x<=n:
        s+=x
    if y_a==y_a[::-1] and y<=n:
        s+=y
print(s) 
    