X,Y=map(int, input().split())
S=0
for i in range(1,7):
    for j in range(1,7):
        if i+j>=X or abs(i-j)>=Y:
            S+=1
print(S/36)