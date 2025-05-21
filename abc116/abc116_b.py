s=int(input())
S=[s]
m=1
while True:
    m+=1
    if s%2==0:
        s=s//2
    else:
        s=3*s+1
    if s in S:
        print(m)
        exit()
    S.append(s)