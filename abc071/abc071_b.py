S=input()
A=[chr(ord("a")+i) for i in range(26)]
s=1
for i in A:
	if i not in S:
		s=i
		break
if s==i:
	print(i)
else:
	print("None")
