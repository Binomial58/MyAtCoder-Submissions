S=input()
K=15-len(S)
if K+S.count("o")>=8:
    print("YES")
else:
    print("NO")