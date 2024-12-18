A,B=map(int, input().split())
if abs(A-B)>1 or A==3 or A==6 or A==9:
    print("No")
else:
    print("Yes")