S=input()
C=[]
#指定された要素を持つインデックスを返す
B=[i for i, x in enumerate(S) if x=="|"]
for k in range(len(S)):
    if k<B[0] or B[1]<k:
        C.append(S[k])
print("".join(C))