A,B=map(int, input().split())
C=[i for i in range(2,14)]
C.append(1)
if C.index(A)>C.index(B):
    print("Alice")
elif C.index(A)<C.index(B):
    print("Bob")
else:
    print("Draw")