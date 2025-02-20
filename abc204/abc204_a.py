Z=set(map(int, input().split()))
X={0,1,2}
if len(Z)==2:
    print(*(X-Z))
else:
    print(*Z)