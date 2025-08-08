def Runlength(S):
    if not S:
        return []
    
    res = []
    prev = S[0]
    count = 1

    for c in S[1:]:
        if c == prev:
            count += 1
        else:
            res.append((prev, count))
            prev = c
            count = 1
    res.append((prev, count))
    return res

n=int(input())
A=list(map(int, input().split()))
runA=Runlength(A)
M=runA[0][0]
T=[]
for i in range(1,len(runA)):
    if M<runA[i][0]:
        M=runA[i][0]
    else:
        break
for a in A:
    if a!=M:
        T.append(a)
print(*T)