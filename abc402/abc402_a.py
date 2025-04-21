S=input()
s=""
for i in range(len(S)):
    if S[i].isupper():
        s+=S[i]
print(s)