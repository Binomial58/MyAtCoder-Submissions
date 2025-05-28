def Lucas(a,b):
    return a+b
L=[2,1]
N=int(input())
for i in range(N-1):
    L.append(Lucas(L[i],L[i+1]))
print(L[-1])