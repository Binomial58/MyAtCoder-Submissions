s=input()
M=0
for i in range(len(s)):
    for j in range(len(s)):
        if i>j:
            continue
        t=s[i:j+1]
        if t[0]=="t" and t[-1]=="t" and t.count("t")>=3:
            M=max(M,(t.count("t")-2)/(len(t)-2))
print(M)