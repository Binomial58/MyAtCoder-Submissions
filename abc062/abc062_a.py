x,y=map(int, input().split())
D=[[1,3,5,7,8,10,12],[4,6,9,11],[2]]
for i in range(3):
    if (x in D[i])and(y in D[i]):
        print("Yes")
        exit()
print("No")