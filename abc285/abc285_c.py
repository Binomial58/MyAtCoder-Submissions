S=input()
B=[chr(i) for i in range(64,91)]
count=0
for i in range(1,len(S)+1):
    b=B.index(S[len(S)-i])
    count+=26**(i-1)*b
print(count)