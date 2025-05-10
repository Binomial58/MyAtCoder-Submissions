S=input()
A=S[:(len(S)-1)//2]
B=S[(len(S)+3)//2-1:]
if S==S[::-1] and A==A[::-1] and B==B[::-1]:
    print("Yes")
else:
    print("No")