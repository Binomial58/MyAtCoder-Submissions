X=int(input())
H=0
H+=X//500*1000
X%=500
H+=X//5*5
print(H)