X=["a","b","c","d","e","f","g","h"]
A=""
for i in range(8,0,-1):
    S=input()
    if S.count("*")!=0:
       A=X[S.index("*")]+str(i)
print(A)