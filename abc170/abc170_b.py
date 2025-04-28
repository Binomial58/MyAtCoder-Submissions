X,Y=map(int, input().split())
for i in range(X+1):
    if Y-i*2==4*(X-i):
        print("Yes")
        exit()
print("No")