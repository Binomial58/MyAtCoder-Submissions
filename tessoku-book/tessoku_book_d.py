n=int(input())
s=""
while n!=1 and n!=0:
    s+=str(n%2)
    n//=2
s+=str(n)
s="0"*(10-len(s))+s[::-1]
print(s)
