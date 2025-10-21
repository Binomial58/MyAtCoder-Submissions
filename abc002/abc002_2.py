w=input()
s=""
B=["a","i","u","e","o"]
for i in w:
    if i not in B:
        s+=i
print(s)