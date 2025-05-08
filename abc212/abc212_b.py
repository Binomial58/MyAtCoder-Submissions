X=input()
C=0
if X[0]==X[1]==X[2]==X[3]:
    print("Weak")
else:
    for i in range(3):
        if (int(X[i])+1)%10==int(X[i+1]):
            C+=1
    if C==3:
        print("Weak")
    else:
        print("Strong")