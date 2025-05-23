S=0
for i in range(3):
    a,b=map(int, input().split())
    S+=a*b//10
print(S)