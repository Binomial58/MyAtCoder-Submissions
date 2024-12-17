N,S,M,L=map(int, input().split())
emin=10**8
for l in range(18):
    for m in range(18):
        for s in range(18):
            if s*6+m*8+l*12>=N:
                price=s*S+m*M+l*L
                emin=min(price,emin)
print(emin)