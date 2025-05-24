E=set(map(int, input().split()))
B=int(input())
L=set(map(int, input().split()))
S=len(E&L)
if S==6:
    print(1)
elif S==5:
    if B in L:
        print(2)
    else:
        print(3)
elif S==4:
    print(4)
elif S==3:
    print(5)
else:
    print(0)