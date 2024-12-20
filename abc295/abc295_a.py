N=int(input())
W=list(map(str, input().split()))
for w in W:
    if w=="and" or  w=="not" or w=="that" or w=="the" or w=="you":
        print("Yes")
        exit()
print("No")