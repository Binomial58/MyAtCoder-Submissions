s=input()
S=set()
for i in s:
    S.add(i)
S=list(S)
if s.count(S[0])==1:
    print(S[0])
else:
    print(S[1])