K=int(input())
S=0
i=1
while i**3<=K:
    j=i
    while i*j**2<=K:
        k=j
        while k*i*j<=K:
            l=set([i,j,k])
            if len(l)==1:
                S+=1
            elif len(l)==2:
                S+=3
            else:
                S+=6
            k+=1
        j+=1
    i+=1
print(S)