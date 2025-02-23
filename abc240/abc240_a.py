a,b=map(int, input().split())
if abs(a-b)==1 or (a==1 and b==10) or (b==1 and a==10):
    print("Yes")
else:
    print("No")