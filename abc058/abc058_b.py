O=input()
E=input()
V=""
for i in range(len(E)):
    V+=O[i]
    V+=E[i]
if len(O)!=len(E):
    V+=O[-1]
print(V)