import math
A,B=map(int, input().split())
C=A/B
if abs(math.ceil(C)-C)>abs(math.floor(C)-C):
    print(math.floor(C))
else:
    print(math.ceil(C))