n=list(input())
n=n[::-1]
even=0
odd=0
for i in range(len(n)):
    if i%2==0:
        even+=int(n[i])
    else:
        odd+=int(n[i])
print(odd,even)
