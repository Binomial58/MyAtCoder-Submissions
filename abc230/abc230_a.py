N=int(input())
S="AGC0"
if N<10:
    S=S+"0"+str(N)
    print(S)
elif N<42:
    S+=str(N)
    print(S)
else:
    S+=str(N+1)
    print(S)