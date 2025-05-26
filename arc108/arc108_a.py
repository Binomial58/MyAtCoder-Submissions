def divisor(N):
    i=1
    A=[]
    while i**2<=N:
        if N%i==0:
            A.append(i)
        i+=1
    return A
S,P=map(int, input().split())
for p in divisor(P):
    if p+P//p==S:
        print("Yes")
        exit()
print("No")