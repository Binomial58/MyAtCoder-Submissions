N,Y=map(int,input().split())

for a in range(N+1):
    for b in range(N-a+1):
        c=N-a-b
        if 10000*a+5000*b+1000*c==Y:
            print(a,b,c)
            exit()
print(-1,-1,-1)