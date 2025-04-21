S=input()
T=S[:len(S)//2]
s=0
for i in range(len(S)//2):
    if S[len(S)-i-1]!=T[i]:
        s+=1
print(s)