a,b=map(int, input().split())
P=list(map(int, input().split()))
Q=list(map(int, input().split()))
pin=["x" for i in range(10)]
for p in P:
    pin[p-1]="."
for q in Q:
    pin[q-1]="o"
print(pin[6]+" "+pin[7]+" "+pin[8]+" "+pin[9])
print(" "+pin[3]+" "+pin[4]+" "+pin[5])
print("  "+pin[1]+" "+pin[2])
print("   "+pin[0])