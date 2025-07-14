w,b=map(int, input().split())
S="wbwbwwbwbwbw"*200
i=0
while i!=len(S):
    if S[i:i+w+b].count("w")==w and S[i:i+w+b].count("b")==b:
        print("Yes")
        exit()
    i+=1
print("No")