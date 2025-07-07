S=input()
T=S[0].upper()
for i in range(1,len(S)):
    T+=S[i].lower()
print(T)