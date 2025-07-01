A,V=map(int, input().split())
B,W=map(int, input().split())
T=int(input())
d=abs(A-B)
v=V-W
if v<=0:
    print("NO")
else:
    if d/v<=T:
        print("YES")
    else:
        print("NO")