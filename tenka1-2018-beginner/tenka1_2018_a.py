S=input()
T=""
if len(S)==2:
    print(S)
else:
    for i in range(3):
        T+=S[3-i-1]
    print(T)