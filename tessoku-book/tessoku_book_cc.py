n=input()
s=0
for i in range(len(n)):
    s+=int(n[::-1][i])*2**i
print(s)