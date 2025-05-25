H,M=map(int, input().split())
for t in range(24*60):
    D=str(H)
    E=str(M)
    if len(D)==1:
        D="0"+D
    if len(E)==1:
        E="0"+E
    if 0<=int(D[0]+E[0])<24 and 0<=int(D[1]+E[1])<60:
        print(H,M)
        exit()
    M+=1
    if M==60:
        M=0
        H+=1
        if H==24:
            H=0