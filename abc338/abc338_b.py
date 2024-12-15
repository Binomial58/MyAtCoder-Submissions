from collections import Counter
S=input()
X=Counter(S)
Y=X.most_common()
Y.sort(key=lambda x:(-x[1],x[0]))
print(Y[0][0])