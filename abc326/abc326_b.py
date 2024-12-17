N=int(input())
S=str(N)
a=int(S[0])
b=int(S[1])
c=int(S[2])
while a*b!=c:
    N+=1
    S=str(N)
    a=int(S[0])
    b=int(S[1])
    c=int(S[2])
print(N)