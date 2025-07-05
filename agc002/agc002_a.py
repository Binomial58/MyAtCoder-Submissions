a,b=map(int, input().split())
if a>0:
    print("Positive")
elif a*b<0:
    print("Zero")
else:
    if abs(a-b)%2==0:
        print("Negative")
    else:
        print("Positive")
