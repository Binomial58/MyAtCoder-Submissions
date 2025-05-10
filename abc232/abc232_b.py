S=input()
T=input()
a=ord(T[0])-ord(S[0])
U=""
for i in range(len(S)):
    U+=chr(97+(ord(S[i])-ord("a")+a)%26)
if U==T:
    print("Yes")
else:
    print("No")