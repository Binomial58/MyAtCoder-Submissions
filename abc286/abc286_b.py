N=int(input())
S=input()
B=""
for i in range(N-1):
    B+=S[i]
    if S[i]=="n" and S[i+1]=="a":
        B+="y"
B+=S[-1]
print(B)