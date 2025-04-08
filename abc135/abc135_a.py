A,B=map(int, input().split())
C=abs(A+B)
if C%2==1:
    print("IMPOSSIBLE")
else:
    print(C//2)