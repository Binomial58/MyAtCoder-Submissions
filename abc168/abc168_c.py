import math
A,B,H,M=map(int, input().split())
minute=M/60*360
hour=H/12*360+minute/12
R=min(abs(hour-minute),360-abs(hour-minute))
print(math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(R))))