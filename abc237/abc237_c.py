s=input()
r=0
l=0
for i in range(len(s)):
	if s[i]=="a":
		l+=1
	else:
		break
u=s[::-1]
for i in range(len(s)):
	if u[i]=="a":
		r+=1
	else:
		break
if l>r:
	print("No")
else:
	t=s[l:len(s)-r]
	if t==t[::-1]:
		print("Yes")
	else:
		print("No")