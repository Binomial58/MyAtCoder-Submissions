S=list(input())
T=[]
d=0
for i in range(26):
   T.append(i+1) 
S,T=zip(*sorted(zip(S,T)))
for i in range(25):
   d+=abs(T[i+1]-T[i])
print(d)