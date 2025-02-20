D=input()
E=""
for i in range(len(D)):
    if D[i]=="N":
        E+="S"
    elif D[i]=="S":
        E+="N"
    elif D[i]=="E":
        E+="W"
    elif D[i]=="W":
        E+="E"
print(E)