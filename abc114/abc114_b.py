S=input()
m=1000
for i in range(len(S)-2):
    m=min(m,abs(753-int(S[i:i+3])))
print(m)