B=["O","D","I","Z","S","B"]
A=["0","0","1","2","5","8"]
s=input()
t=""
for i in range(len(s)):
    if s[i]in B:
        t+=A[B.index(s[i])]
    else:
        t+=s[i]
print(t)