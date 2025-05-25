def make_divisors(n):
    i=1
    C=[]
    D=[]
    while i*i<=n:
        if n%i==0:
            C.append(i)
            if n//i!=i:
                D.append(n//i)
        i+=1
    return C+D[::-1]
N=int(input())
E=make_divisors(N)
for e in E:
    print(e)