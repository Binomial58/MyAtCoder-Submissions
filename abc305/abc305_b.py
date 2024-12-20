p,q=map(str, input().split())
X=["A","B","C","D","E","F","G"]
Y=[0,3,4,8,9,14,23]
print(abs(Y[X.index(p)]-Y[X.index(q)]))
