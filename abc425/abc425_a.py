n=int(input())
s=0
for i in range(n):
    s+=(-1)**(i+1)*(i+1)**3
print(s)