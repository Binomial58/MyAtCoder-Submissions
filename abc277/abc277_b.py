N=int(input())
S=[]
K=0
for _ in range(N):
    s=input()
    if s[0] not in["H","D","C","S"]:
        K=1
    if s[1] not in["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
        K=1
    S.append(s)
if len(S)==len(set(S)) and K==0:
    print("Yes")
else:
    print("No")