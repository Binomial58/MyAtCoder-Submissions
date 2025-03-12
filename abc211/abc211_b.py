def Hit(X):
    if X=="H":
        return 1
    elif X=="2B":
        return 2
    elif X=="3B":
        return 3
    else:
        return 4
S=0
for _ in range(4):
    A=input()
    S+=Hit(A)
if S==10:
    print("Yes")
else:
    print("No")