a,b=list(map(str, input().split()))
c=int(a+b)
for i in range(c):
    if i**2==c:
        print("Yes")
        exit()
print("No")
    