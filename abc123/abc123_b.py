A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
X=[A,B,C,D,E]
m=10
I=0
S=0
for i in range(5):
    if X[i]%10!=0:
        if m>X[i]%10:
            I=i
            m=X[i]%10
for i in range(5):
    if i!=I:
        if X[i]%10!=0:
            S+=10*(X[i]//10+1)
        else:
            S+=X[i]
    else:
        S+=X[i]
print(S)