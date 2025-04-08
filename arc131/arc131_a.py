A=input()
B=int(input())
C=str(B//2)
if int(B)%2==1:
    print(int(A+"0"+str(int(B/2*10))))
else:
    print(A+"0"+C)