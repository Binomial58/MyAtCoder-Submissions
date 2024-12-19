M=int(input())
D=list(map(int, input().split()))
A=(sum(D)+1)//2
m=0
d=0
while d<A:
    d+=D[m]
    m+=1
print(m,D[m-1]-d+A)