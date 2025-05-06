day=input()
D=[0,"Friday","Thursday","Wednesday","Tuesday","Monday"]
if day not in D:
    print(0)
else:
    print(D.index(day))