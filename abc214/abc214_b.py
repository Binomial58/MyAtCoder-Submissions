S,T=map(int, input().split())
R=0
for a in range(S+1):
    for b in range(S+1-a):
        for c in range(S+1-a-b):
            if a*b*c<=T:
                R+=1
print(R)