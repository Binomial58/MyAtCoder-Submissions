s=input()
S=0
F=0
for i in s:
    if i=="C" and F==0:
        S=1
    elif i=="F" and S==1:
        F=1
if S==1 and F==1:
    print("Yes")
else:
    print("No")