A=input()
B=input()
C=input()
T=input()
S=""
for i in range(len(T)):
    if T[i]=="1":
        S+=A
    elif T[i]=="2":
        S+=B
    else:
        S+=C
print(S)