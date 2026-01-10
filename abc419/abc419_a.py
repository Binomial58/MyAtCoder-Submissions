s = input()
A = ["red", "blue", "green"]
B = ["SSS", "FFF", "MMM"]
if s in A:
    print(B[A.index(s)])
else:
    print("Unknown")
