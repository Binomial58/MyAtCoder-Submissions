N=input()
for i in range(len(N)-1):
    a=int(N[i])
    b=int(N[i+1])
    if a<=b:
        print("No")
        exit()
print("Yes")