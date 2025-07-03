N=int(input())
i=1
V=[]
while i**3<=N:
    V.append(i**3)
    i+=1
V.sort(reverse=True)
for v in V:
    v=str(v)
    if v==v[::-1]:
        print(v)
        exit()