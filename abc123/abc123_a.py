a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
X=[a,b,c,d,e]
for i in X:
    for j in X:
        if max(i-j,j-i)>k:
            print(":(")
            exit()
print("Yay!")
