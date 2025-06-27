S=input()
T=input()
for i in range(len(S)):
    if S==T:
        print("Yes")
        exit()
    T=T[1:]+T[0]
print("No")