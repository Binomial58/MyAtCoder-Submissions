N=input()
M=""
for i in range(3):
    if N[i]=="1":
        M+="9"
    elif N[i]=="9":
        M+="1"
    else:
        M+=N[i]
print(M)