def Equation(x):
    return x**3+x
n=int(input())
l=0
r=100000
x=(r+l)/2
while abs(Equation(x)-n)>=0.001:
    if Equation(x)>=n:
        r=x
        x=(r+l)/2
    else:
        l=x
        x=(r+l)/2
print(x)