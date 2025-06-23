import math
a,b,d=map(int, input().split())
r=math.radians(d)
A=math.cos(r)*a-math.sin(r)*b
B=math.sin(r)*a+math.cos(r)*b
print(A,B)