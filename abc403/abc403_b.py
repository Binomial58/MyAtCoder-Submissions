T=input()
U=input()
for i in range(len(T)-len(U)+1):
    s=0
    for j in range(len(U)):
        if T[i+j]==U[j] or T[i+j]=="?":
            s+=1
        else:
            break
    if s==len(U):
       print("Yes")
       exit()
print("No")
