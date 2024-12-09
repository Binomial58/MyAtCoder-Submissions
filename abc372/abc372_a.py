S=input()
S=list(S)
L=len(S)
for i in range(L):
    if S[i]==".":
        S[i]=""
#リストを文字列に変換
R="".join(S)
print(R)