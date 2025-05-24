A=int(input())
B=int(input())
C=int(input())
R=[A,B,C]
R.sort(reverse=True)
print(R.index(A)+1)
print(R.index(B)+1)
print(R.index(C)+1)