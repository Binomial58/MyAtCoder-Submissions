N=int(input())
S=input()
B=[chr(i) for i in range(65,91)]
T=""
for i in range(len(S)):
    T+=B[(B.index(S[i])+N)%26]
print(T)