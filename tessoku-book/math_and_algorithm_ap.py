n=int(input())
F=[1,1]
for i in range(n-2):
    F.append((F[i]+F[i+1])%1000000007)
print(F[-1])