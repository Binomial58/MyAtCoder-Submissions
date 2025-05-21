H=int(input())
S=0
i=0
while H!=0:
    S+=2**i
    H//=2
    i+=1
print(S)