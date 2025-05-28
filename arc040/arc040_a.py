N=int(input())
R=0
B=0
for i in range(N):
    s=input()
    R+=s.count("R")
    B+=s.count("B")
if R>B:
    print("TAKAHASHI")
elif R<B:
    print("AOKI")
else:
    print("DRAW")