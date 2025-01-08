N,K=map(int, input().split())
S=input()
T=""
count=0
for i in range(N):
    if S[i]=="o" and count<K:
        T+="o"
        count+=1
    else:
        T+="x"
print(T)