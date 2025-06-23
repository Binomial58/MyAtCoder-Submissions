A=int(input())  
i=1
while i*i*i<=A:
    if i*i*i==A:
        print("YES")
        exit()
    i+=1
print("NO")