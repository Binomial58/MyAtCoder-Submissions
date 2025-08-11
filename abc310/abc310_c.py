n=int(input())
S=set()
for i in range(n):
    s=input()
    Ms=max(s,s[::-1])
    S.add(Ms)
print(len(S))