X=input()
S=""
for i in range(len(X)):
    if X[i]!=".":
        S+=X[i]
    else:
        break
print(S)